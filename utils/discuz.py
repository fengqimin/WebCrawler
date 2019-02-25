# -*- coding: utf-8 -*-
"""实现Discuz!论坛的自动登录"""
import requests

from HKPicCrawler.hkpicconfig import BASE_URL, HOST, SEARCH_HREF

USERNAME = 'hktest'
PASSWORD = 'HKPic:PEP-3156/tulip'


# email = 'bstest3156@outlook.com'
# email_pw = '3156/tulip'
# 英国，1990-1-17


class DiscuzRobot:
    """实现Discuz!论坛的自动登录

    """

    def __init__(self, host=HOST, username=USERNAME, password=PASSWORD):
        """

        :param host:
        :param username:
        :param password:
        """
        self.host = host
        # 会员url
        self._member_href = 'http://{host}/member.php'.format(host=self.host)
        self._misc_href = 'http://{host}/misc.php'.format(host=self.host)
        # 登录窗口的url地址
        self._login_window_url = \
            self._member_href + '?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
        self._login_hash = ''
        self._form_hash = ''
        self._update = None
        self.session = requests.session()
        self._username = username
        self._password = password
        self._code = ''
        self._headers = {
            'Host': '{host}'.format(host=self.host),
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://{host}/forum.php'.format(host=self.host),
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8'}
        self.headers = None
        self.cookies = None

    def get_login_window(self):
        """# 获取登录窗口中的loginhash和self._form_hash
        """

        # 清空原来的headers
        self.session.headers.clear()
        # 更新headers
        self.session.headers.update(self._headers)
        try:
            _r = self.session.get(self._login_window_url)
        except IOError as e:
            print('ERROR：', e)
            return
        print(_r.status_code)
        # 获取loginhash
        _pos = _r.text.find('loginhash') + len('loginhash') + 1
        self._login_hash = _r.text[_pos:_pos + 5]
        # 获取formhash
        _pos = _r.text.find('formhash') + len('formhash" value="')
        self._form_hash = _r.text[_pos:_pos + 8]
        return self._login_hash, self._form_hash

    def get_code_info(self):
        """# 获取update"""
        _url = '{0}?mod=seccode&action=update&idhash=cSA&0.3916181418197131&modid=member::logging'.format(
            self._misc_href)
        _r = self.session.get(_url)
        _pos = _r.text.find('update=')
        self._update = _r.text[_pos + 7:_pos + 12]

    def get_code(self):
        """# 获取验证码"""
        self.get_code_info()
        _url = '{0}?mod=seccode&update={1}&idhash=cSA'.format(
            self._misc_href, self._update)
        self.session.headers.clear()
        self.session.headers.update(self._headers)
        _r = self.session.get(_url)
        if _r.content[:3] == b'GIF':
            # 保存验证码图片
            file = open('code.gif', 'wb')
            file.write(_r.content)
            file.close()
        else:
            # 打印错误信息
            print(_r.text)

    def check_code(self):
        """# 检查验证码是否正确
        # 通过人工识别验证码code，:)

        """
        code = input()
        _url = '{0}?mod=seccode&action=check&inajax=1&modid=member::logging&idhash=cSA&secverify={1}'.format(
            self._misc_href, code)

        self.session.headers.clear()
        self.session.headers.update(self._headers)
        _r = self.session.get(_url)
        return _r.text

    def login(self, code=''):
        """# 模拟登录
        :type code: str
        """
        self.get_login_window()
        # self.get_code()
        # self.check_code()
        login_url = '{0}?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash={1}&inajax=1'.format(
            self._member_href, self._login_hash)

        data = {'formhash': self._form_hash,
                'referer': 'http://{host}/forum.php'.format(host=self.host),
                'loginfield': 'username',
                'username': self._username,
                'password': self._password,
                'questionid': '0',
                'answer': '',
                'seccodehash': 'cSA',
                'seccodemodid': 'member::logging',
                'seccodeverify': code}

        self.session.headers.clear()
        self.session.headers.update(self._headers)
        _r = self.session.post(login_url, data)
        self.headers = self.session.headers
        self.cookies = self.session.cookies

    def search(self, kw):
        """search"""
        url = BASE_URL + SEARCH_HREF
        '''表单数据
        formhash	3d71a5bf
        searchsubmit	yes
        srchtxt	长腿
        '''

        '''请求头：
        Host: 174.138.175.178
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Accept-Encoding: gzip, deflate
        Referer: http://174.138.175.178/search.php?mod=forum
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 61
        Cookie: Ovo6_2132_ulastactivity=1526835463%7C0; Ovo6_2132_auth=c390bm8XTQ9IshlZs6WIay5zeQPCYzXUShq2Ugi5TnKsT8Chc0DK3dKgG3TYO96orCYO%2BoLq7AgFABZkqrt%2BdFlrCfU; Ovo6_2132_lastcheckfeed=656492%7C1526047026; Ovo6_2132_nofavfid=1; Ovo6_2132_forum_lastvisit=D_780_1523683424D_776_1523967620D_454_1523967726D_106_1524566363D_769_1524566607D_770_1524567522D_764_1524567564D_36_1524670980D_122_1524748821D_628_1525016551D_637_1525016648D_758_1525017394D_636_1525151921D_192_1525163296D_186_1525163315D_645_1525271293D_102_1525363595D_42_1525363818D_212_1525428530D_232_1525430095D_43_1525438700D_44_1525530458D_66_1525543483D_433_1525544124D_110_1525792357D_142_1525877061D_239_1526089799D_126_1526089903D_423_1526130935D_294_1526476890D_135_1526476922D_193_1526477041D_79_1526478584D_2_1526481542D_10_1526827250D_30_1526831728D_18_1526834479D_398_1526834942; Ovo6_2132_visitedfid=398D18D30D10D39D2D79D193D135D294; Ovo6_2132_collapse=_forum_rules_18__forum_rules_10__forum_rules_454__forum_rules_30__forum_rules_398__forum_rules_102__forum_rules_135__forum_rules_628__forum_rules_637__forum_rules_142__forum_rules_636__forum_rules_79__forum_rules_239__forum_rules_645__forum_rules_44__forum_rules_66__forum_rules_433__forum_rules_110__forum_rules_193_; Ovo6_2132_forumdefstyle=1; Ovo6_2132_smile=1D1; Ovo6_2132_lastrequest=685f4G%2FjOasbU8NExwpeIbUielWMlbUD%2BQvd93RQ5uq2qvcxfMeG; Ovo6_2132_saltkey=PGG5l23E; Ovo6_2132_lastvisit=1525874109; Ovo6_2132_widthauto=1; Ovo6_2132_lastact=1526835471%09search.php%09forum; PHPSESSID=7o7ur9n8qjbr8a8pbbb1om15d5; Ovo6_2132_home_diymode=1; Ovo6_2132_viewid=tid_4984902; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_checkpm=1; Ovo6_2132_sendmail=1
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        '''
        data = {'formhash': self._form_hash,
                'searchsubmit': 'yes',
                'srchtxt': kw,
                }
        _r = self.session.post(url, data)
        # print(_r.text)
        return _r
