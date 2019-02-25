# -*- coding: utf-8 -*-
"""request

 """
from framework.utils.useragent import random_ua

ZHIHU_HEADERS = """
    Host: www.zhihu.com
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate
    Referer: https://www.zhihu.com/
    Connection: keep-alive
    Cookie: q_c1=9b2fc2372ae04cc588e4dc886d8b471a|1530944322000|1523090396000; _zap=3f9026af-7dc4-477f-aa13-4dccba5b2cd1; aliyungf_tc=AQAAAL5HSD8NfQUAQVJxe4FsQhauhDZP; _xsrf=2f851a7a-ab86-4aea-89d7-3cd2007d4960; d_c0="AFAgkXDkZw2PTjWNiDZNXhX4zC3B0w1Ho6w=|1523090396"; l_n_c=1; n_c=1; tgw_l7_route=66cb16bc7f45da64562a077714739c11; capsion_ticket="2|1:0|10:1547904692|14:capsion_ticket|44:MmQ2NjQxZGEzOWNkNDk3ODlmYWRjZDM4YmU0NzZjNzg=|c630c76b9a6033ddc8610dbb59aa73aeaf29c54df86418a29ffa775e598f6698"; z_c0="2|1:0|10:1547904719|4:z_c0|92:Mi4xQldLdEFnQUFBQUFBVUNDUmNPUm5EU1lBQUFCZ0FsVk56M1F3WFFBaURXMGxtSm54Y1pROXVkejdGeEpOYU4ycGhR|d3fafd5b9d91fef252dca86d4ce2dd718a095e1de8d5927f056daa5448169fb9"; unlock_ticket="ABDKhNkChwkmAAAAYAJVTdctQ1wICyCQOTtBNIy3tNWYdRJ5ywMgRA=="; tst=r
    Upgrade-Insecure-Requests: 1
    Pragma: no-cache
    Cache-Control: no-cache
    """
__all__ = ["fake_headers", "str2cookies", "str2headers", "cookies2str"]


def fake_headers(*, host='', user_agent='', referer='', cookies=''):
    _headers = {
        'Host': host,
        'Connection': 'keep-alive',
        'User-Agent': user_agent or random_ua(),
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Referer': referer,
        'Cookie': cookies,
    }

    retval = {}
    for k, v in _headers.items():
        if v:
            retval[k] = v

    return retval


def str2headers(string: str):
    """把从浏览器上拷贝过来的headers字符串变为headers字典

    :param string:str
    :return: _d:dict
    """
    '''
        Host: 174.138.175.178
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
        Accept: text/css,*/*;q=0.1
        Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
        Accept-Encoding: gzip, deflate
        Referer: http://174.138.175.178/forum.php
        Connection: keep-alive
        Cookie: Ovo6_2132_ulastactivity=1550939128%7C0; Ovo6_2132_lastcheckfeed=656492%7C1550412445; Ovo6_2132_nofavfid=1; Ovo6_2132_visitedfid=18D2D398D153D193D30D126D79D10D454; Ovo6_2132_smile=1D1; Ovo6_2132_forumdefstyle=1; Ovo6_2132_forum_lastvisit=D_43_1548490218D_102_1548567520D_2_1548950943D_39_1549109971D_765_1549627115D_135_1549630440D_142_1549785018D_239_1549901338D_294_1550070710D_764_1550391345D_454_1550676830D_10_1550677141D_30_1550756371D_79_1550769810D_126_1550769999D_193_1550858640D_153_1550860535D_398_1550909750D_18_1550935248; Ovo6_2132_collapse=_forum_rules_18__forum_rules_135__forum_rules_142__forum_rules_30__forum_rules_398__forum_rules_454__forum_rules_79__forum_rules_153_; Ovo6_2132_widthauto=1; Ovo6_2132_saltkey=F84l22Yi; Ovo6_2132_lastvisit=1550408806; Ovo6_2132_auth=a1089TNfs7BQQ%2BuASGxBMaA%2F1jQ%2B1k8EFfs76TCKKCLYSCEwBassrnU8mbIR3YfPX9iqwJ7couJZQH3c9MY7OHg2tlI; Ovo6_2132_lastact=1550939128%09forum.php%09; PHPSESSID=7o7ur9n8qjbr8a8pbbb1om15d5; Ovo6_2132_secqaaS00=c511pcgoI4v3WKlIvwOCwwTF4o91MHFWuM8C9qOkd%2Fi%2FSHor5ZvRHPZzcgAld57ytvAx3KETwB3j9tbu6gVtmbLl9dyyBJHd3k72HcvCkoRJtrR79w; Ovo6_2132_home_diymode=1; Ovo6_2132_k_pwchangetipsendmail=1532219755; Ovo6_2132_viewid=tid_5498153; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_creditnotice=0D0D2D0D0D0D0D0D0D656492; Ovo6_2132_creditbase=0D384D12196D0D0D0D0D0D0; Ovo6_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E9%8C%84
        Pragma: no-cache
        Cache-Control: no-cache
        '''
    _d = dict()
    for item in string.splitlines():
        if item:
            k, v = item.split(':', 1)
            _d.update([(k, v.strip())])
    return _d


def str2cookies(string: str):
    _cookie = dict()
    for item in string.split():
        if item:
            k, v = item.split('=', 1)
            _cookie.update([(k, v.strip(';'))])
    return _cookie


def cookies2str(cookies: dict):
    _retval = ''
    for k, v in cookies.items():
        _retval = _retval + str(k) + '=' + str(v) + '; '

    return _retval.strip('; ')


class Request:
    pass


if __name__ == '__main__':
    c = 'Ovo6_2132_ulastactivity=1550939895%7C0; Ovo6_2132_lastcheckfeed=656492%7C1550412445; Ovo6_2132_nofavfid=1; Ovo6_2132_visitedfid=2D18D398D153D193D30D126D79D10D454; Ovo6_2132_smile=1D1; Ovo6_2132_forumdefstyle=1; Ovo6_2132_forum_lastvisit=D_43_1548490218D_102_1548567520D_2_1548950943D_39_1549109971D_765_1549627115D_135_1549630440D_142_1549785018D_239_1549901338D_294_1550070710D_764_1550391345D_454_1550676830D_10_1550677141D_30_1550756371D_79_1550769810D_126_1550769999D_193_1550858640D_153_1550860535D_398_1550909750D_18_1550935248; Ovo6_2132_collapse=_forum_rules_18__forum_rules_135__forum_rules_142__forum_rules_30__forum_rules_398__forum_rules_454__forum_rules_79__forum_rules_153_; Ovo6_2132_widthauto=1; Ovo6_2132_saltkey=F84l22Yi; Ovo6_2132_lastvisit=1550408806; Ovo6_2132_auth=a1089TNfs7BQQ%2BuASGxBMaA%2F1jQ%2B1k8EFfs76TCKKCLYSCEwBassrnU8mbIR3YfPX9iqwJ7couJZQH3c9MY7OHg2tlI; Ovo6_2132_lastact=1550940127%09forum.php%09viewthread; PHPSESSID=7o7ur9n8qjbr8a8pbbb1om15d5; Ovo6_2132_secqaaS00=c511pcgoI4v3WKlIvwOCwwTF4o91MHFWuM8C9qOkd%2Fi%2FSHor5ZvRHPZzcgAld57ytvAx3KETwB3j9tbu6gVtmbLl9dyyBJHd3k72HcvCkoRJtrR79w; Ovo6_2132_home_diymode=1; Ovo6_2132_k_pwchangetipsendmail=1532219755; Ovo6_2132_viewid=tid_5496172; Ovo6_2132_myrepeat_rr=R0; Ovo6_2132_checkpm=1; Ovo6_2132_sendmail=1'
    d = {'Ovo6_2132_lastact': '1550942799%09forum.php%09viewthread',
         'Ovo6_2132_ulastactivity': '1550942799%7C0',
         'Ovo6_2132_viewid': 'tid_5458891',
         'Ovo6_2132_visitedfid': '18D2D398D153D193D30D126D79D10D454'}

    # print(resp.headers)
    # print(dict(resp.cookies.items()))
    d_c = str2cookies(c)
    d_c.update(d)

    headers = fake_headers(host='174.138.175.178',
                           user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
                           referer='',
                           cookies=cookies2str(d_c)
                           )
    import requests

    resp = requests.get('http://174.138.175.178/thread-5458891-1-1.html', headers=headers)
    print(resp, resp.text)
    print(resp.cookies.items())
