# -*- coding: utf-8 -*-
# Author: FengQiMin<fengqimin@msn.com>
# Created on 2019-01-08 00:15:13
"""获取免费的高匿proxy

    ('HTTP', '116.209.54.174', '9999')

    66ip.cn
    data5u.com
    ip181.com
    xicidaili.com
    goubanjia.com
    xdaili.cn
    kuaidaili.com
    cn-proxy.com
    proxy-list.org
    www.mimiip.com
    """

import gzip
import re
import urllib.request
from urllib.parse import urlsplit

from framework.utils.request import fake_headers

# import zlib
PROXIES = {
    'xicidaili': [('HTTP', '116.209.55.7', '9999'), ('HTTP', '183.148.154.241', '9999'),
                  ('HTTP', '112.85.128.184', '9999'), ('HTTP', '116.209.59.223', '9999'),
                  ('HTTP', '49.86.183.13', '9999'), ('HTTP', '117.93.159.138', '9999'),
                  ('HTTPS', '111.177.186.195', '9999'), ('HTTPS', '116.209.55.167', '9999'),
                  ('HTTP', '125.126.204.79', '9999'), ('HTTP', '125.126.223.206', '9999'),
                  ('HTTP', '124.94.195.49', '9999'), ('HTTP', '111.177.189.79', '9999'),
                  ('HTTPS', '111.177.169.224', '9999'), ('HTTP', '112.85.164.23', '9999'),
                  ('HTTP', '110.52.235.64', '9999'), ('HTTPS', '182.44.220.124', '9999'),
                  ('HTTPS', '111.177.181.61', '9999'), ('HTTPS', '111.72.154.241', '9999'),
                  ('HTTPS', '115.151.3.25', '9999'), ('HTTPS', '111.177.174.249', '9999'),
                  ('HTTPS', '222.189.191.217', '9999'), ('HTTP', '183.148.148.73', '9999'),
                  ('HTTP', '116.209.53.22', '9999'), ('HTTP', '115.46.65.26', '8123'),
                  ('HTTP', '116.209.53.225', '9999'), ('HTTP', '111.177.113.240', '9999'),
                  ('HTTP', '111.177.189.4', '9999'), ('HTTPS', '125.123.141.86', '9999'),
                  ('HTTPS', '112.85.166.23', '9999'), ('HTTPS', '110.52.235.204', '9999'),
                  ('HTTPS', '183.148.130.2', '9999'), ('HTTPS', '110.52.235.26', '9999'),
                  ('HTTP', '110.52.235.14', '9999'), ('HTTP', '112.84.54.58', '9999'),
                  ('HTTPS', '60.190.66.131', '56882'), ('HTTP', '1.198.73.194', '9999'),
                  ('HTTPS', '163.204.243.60', '9999'), ('HTTPS', '183.148.142.211', '9999'),
                  ('HTTPS', '112.87.67.100', '9999'), ('HTTPS', '116.209.59.169', '9999'),
                  ('HTTPS', '183.148.130.31', '9999'), ('HTTPS', '118.76.235.98', '8118'),
                  ('HTTP', '115.46.97.82', '8123'), ('HTTP', '117.95.199.33', '9999'),
                  ('HTTP', '59.62.167.242', '9999'), ('HTTPS', '121.61.1.108', '9999'),
                  ('HTTPS', '125.126.220.200', '9999'), ('HTTPS', '183.148.139.99', '9999'),
                  ('HTTP', '121.61.0.178', '9999'), ('HTTPS', '27.29.79.70', '9999'),
                  ('HTTP', '110.52.235.193', '9999'), ('HTTPS', '112.85.167.2', '9999'),
                  ('HTTP', '183.148.141.237', '9999'), ('HTTP', '113.122.169.61', '9999'),
                  ('HTTP', '183.148.139.146', '9999'), ('HTTP', '115.151.4.142', '9999'),
                  ('HTTP', '116.209.53.19', '9999'), ('HTTPS', '183.148.134.118', '9999'),
                  ('HTTPS', '125.126.217.108', '9999'), ('HTTPS', '111.77.196.168', '9999'),
                  ('HTTP', '112.85.151.162', '9999'), ('HTTP', '171.38.76.156', '8123'),
                  ('HTTP', '116.209.57.166', '9999'), ('HTTP', '116.209.58.101', '9999'),
                  ('HTTP', '111.177.165.245', '9999'), ('HTTP', '116.209.52.48', '9999'),
                  ('HTTP', '125.123.142.40', '9999'), ('HTTP', '121.61.3.77', '9999'),
                  ('HTTPS', '110.52.235.144', '9999'), ('HTTP', '125.126.195.198', '9999'),
                  ('HTTPS', '111.177.167.108', '9999'), ('HTTPS', '125.123.137.247', '9999'),
                  ('HTTPS', '112.85.167.47', '9999'), ('HTTPS', '112.87.68.54', '9999'),
                  ('HTTP', '121.61.2.62', '9999'), ('HTTP', '125.123.140.2', '9999'),
                  ('HTTPS', '111.177.173.95', '9999'), ('HTTPS', '61.142.72.150', '39894'),
                  ('HTTP', '121.61.0.62', '9999'), ('HTTP', '27.29.45.113', '9999'),
                  ('HTTPS', '125.126.203.29', '9999'), ('HTTP', '27.29.45.213', '9999'),
                  ('HTTP', '125.126.201.205', '9999'), ('HTTP', '111.177.165.94', '9999'),
                  ('HTTPS', '111.177.169.0', '9999'), ('HTTP', '111.177.177.229', '9999'),
                  ('HTTP', '182.88.190.188', '8123'), ('HTTP', '111.177.185.187', '9999'),
                  ('HTTP', '112.85.128.100', '9999'), ('HTTPS', '27.29.44.254', '9999'),
                  ('HTTPS', '27.29.45.137', '9999'), ('HTTP', '110.52.235.131', '9999'),
                  ('HTTPS', '115.151.4.206', '9999'), ('HTTPS', '27.29.44.196', '9999'),
                  ('HTTP', '116.209.55.216', '9999'), ('HTTP', '1.192.242.153', '9999'),
                  ('HTTP', '221.235.233.238', '9999'), ('HTTP', '171.80.155.220', '9999'),
                  ('HTTPS', '59.62.165.123', '9999'), ('HTTP', '125.126.211.216', '9999')],
    '66ip': [('HTTPS', '54.36.9.176', '1080'), ('HTTPS', '115.239.25.165', '9999'), ('HTTPS', '59.62.167.215', '9999'),
             ('HTTPS', '187.178.238.177', '54340'), ('HTTPS', '111.177.174.33', '9999'),
             ('HTTPS', '111.177.167.119', '9999'), ('HTTPS', '112.85.169.239', '9999'),
             ('HTTPS', '171.12.115.57', '9999'), ('HTTPS', '115.203.96.93', '9999'),
             ('HTTPS', '202.57.54.226', '34911'), ('HTTPS', '91.83.88.1', '49716'), ('HTTPS', '117.90.1.47', '9999'),
             ('HTTPS', '111.177.191.232', '9999'), ('HTTPS', '121.232.148.109', '9999'),
             ('HTTPS', '125.123.140.212', '9999'), ('HTTPS', '1.198.73.112', '9999'),
             ('HTTPS', '182.44.221.177', '9999'), ('HTTPS', '113.128.25.249', '9999'),
             ('HTTPS', '116.209.55.228', '9999'), ('HTTPS', '188.92.242.180', '52048'),
             ('HTTPS', '123.163.117.158', '9999'), ('HTTPS', '60.13.42.116', '9999'),
             ('HTTPS', '123.55.114.230', '9999'), ('HTTPS', '111.177.176.130', '9999'),
             ('HTTPS', '121.61.26.91', '9999'), ('HTTPS', '84.244.7.52', '5220'), ('HTTPS', '111.177.180.95', '9999'),
             ('HTTPS', '114.6.94.84', '8080'), ('HTTPS', '123.55.114.243', '9999'), ('HTTPS', '5.16.8.14', '8080'),
             ('HTTPS', '111.177.162.210', '9999'), ('HTTPS', '58.55.206.20', '9999'),
             ('HTTPS', '93.190.137.58', '8080'), ('HTTPS', '180.107.248.204', '9999'),
             ('HTTPS', '163.204.245.130', '9999'), ('HTTPS', '58.55.140.167', '9999'),
             ('HTTPS', '163.204.244.215', '9999'), ('HTTPS', '123.101.207.199', '9999'),
             ('HTTPS', '178.33.9.99', '1080'), ('HTTPS', '181.143.157.242', '50942'), ('HTTPS', '1.197.203.69', '9999'),
             ('HTTPS', '163.204.246.224', '9999'), ('HTTPS', '115.151.4.105', '9999'),
             ('HTTPS', '123.163.118.58', '9999'), ('HTTPS', '114.104.135.85', '9999'),
             ('HTTPS', '123.55.101.206', '9999'), ('HTTPS', '111.177.188.200', '9999'),
             ('HTTPS', '180.118.77.31', '9999'), ('HTTPS', '139.255.17.2', '47421'), ('HTTPS', '113.121.145.0', '9999'),
             ('HTTPS', '111.177.183.168', '9999'), ('HTTPS', '180.118.216.231', '9999'),
             ('HTTPS', '111.177.176.27', '9999'), ('HTTPS', '134.119.205.162', '8080'),
             ('HTTPS', '116.209.56.144', '9999'), ('HTTPS', '222.189.144.159', '9999'),
             ('HTTPS', '180.118.128.54', '9999'), ('HTTPS', '123.163.116.55', '9999'),
             ('HTTPS', '179.182.211.54', '8080'), ('HTTPS', '123.55.102.65', '9999'),
             ('HTTPS', '163.204.241.196', '9999'), ('HTTPS', '27.29.74.245', '9999'),
             ('HTTPS', '111.177.179.111', '9999'), ('HTTPS', '145.239.169.46', '1080'),
             ('HTTPS', '111.177.186.184', '9999'), ('HTTPS', '111.177.178.152', '9999'),
             ('HTTPS', '113.121.157.22', '9999'), ('HTTPS', '49.86.183.191', '9999'),
             ('HTTPS', '123.55.106.245', '9999'), ('HTTPS', '115.203.97.200', '9999'),
             ('HTTPS', '114.239.253.211', '9999'), ('HTTPS', '212.126.107.2', '31475'),
             ('HTTPS', '36.26.227.53', '9999'), ('HTTPS', '116.209.54.239', '9999'),
             ('HTTPS', '163.204.240.43', '9999'), ('HTTPS', '111.177.162.40', '9999'),
             ('HTTPS', '114.239.148.230', '9999'), ('HTTPS', '110.52.235.192', '9999'),
             ('HTTPS', '183.15.122.139', '3128'), ('HTTPS', '212.129.3.187', '54321'),
             ('HTTPS', '114.239.149.210', '9999'), ('HTTPS', '109.197.184.7', '8080'),
             ('HTTPS', '180.118.242.52', '9999'), ('HTTPS', '111.177.161.234', '9999'),
             ('HTTPS', '124.94.198.165', '9999'), ('HTTPS', '195.25.111.21', '3128'),
             ('HTTPS', '58.55.193.121', '9999'), ('HTTPS', '103.254.127.202', '88'), ('HTTPS', '115.42.34.220', '8080'),
             ('HTTPS', '111.177.182.137', '9999'), ('HTTPS', '163.204.245.222', '9999'),
             ('HTTPS', '182.44.220.63', '9999'), ('HTTPS', '123.160.74.235', '9999'),
             ('HTTPS', '111.177.160.105', '9999'), ('HTTPS', '113.121.145.110', '9999'),
             ('HTTPS', '113.122.169.140', '9999'), ('HTTPS', '140.143.142.218', '1080'),
             ('HTTPS', '183.148.139.49', '9999'), ('HTTPS', '183.166.137.142', '9999'),
             ('HTTPS', '111.177.178.226', '9999')],

}

DATA_PATH = r'D:\My Projects\Python\WebCrawler\data'
# 免费代理站点
SITE = {
    '66ip': {
        'index': 'http://www.66ip.cn/nm.html',
        'url': '',
        're': '',
    },
    'xicidaili': {
        'index': 'https://www.xicidaili.com/nn/',
        'url': '',
        're': '',
    },
}

PROXY_TYPE = [
    'HTTP',
    'HTTPS',
    'HTTP or HTTPS'
]

REGEX_XICIDAILI = re.compile(r'(?is)<td>(\d+\.\d+\.\d+\.\d+)</td>.*?<td>(\d+)</td>.*?<td>(HTTP|HTTPS)</td>')
REGEX_66IP = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})')


class ProxyPool:

    def __init__(self):
        pass

    def fetch_proxies_from_66ip(self):
        pass

    def fetch_proxies_from_xicidili(self):
        pass


def fetch_proxies_from_66ip(get_num=100, proxy_type=1):
    """抓取代理66 http://www.66ip.cn/

        http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=66ip
        66ip存在521陷阱，因此使用webdriver调用firefox进行访问。
            # from selenium import webdriver
            # options = webdriver.FirefoxOptions()
            # # 无头模式
            # options.headless = True
            # browser = webdriver.Firefox(options=options)
            # browser.get(url)
            # # time.sleep(10)
            # # browser.implicitly_wait(10)
            # html = browser.page_source
            # browser.quit()
        @:param:get_num:int,提取数量
        @:param:proxy_type:int,代理类型,0-http 1-https 2-both
        anonymoustype=4
        :return:
        """

    url = f"http://www.66ip.cn/nmtq.php?getnum={get_num}&isp=0&anonymoustype=4&start=&ports=&export=&ipaddress=&area=0&proxytype={proxy_type}&api=66ip"
    req = urllib.request.Request(url, headers=fake_headers())
    resp = urllib.request.urlopen(req)
    content = resp.read()
    html = gzip.decompress(content)

    proxies = REGEX_66IP.findall(html.decode('gbk'))
    retval = []
    for proxy in proxies:
        retval.append((PROXY_TYPE[proxy_type], proxy[0], proxy[1]))

    return retval


def fetch_proxies_from_xicidaili(page=1):
    # url = 'http://www.xicidaili.com/nt/{}'.format(page)
    url = 'https://www.xicidaili.com/nn/{}'.format(page)

    req = urllib.request.Request(url, headers=fake_headers())
    resp = urllib.request.urlopen(req)
    content = resp.read()
    # try:
    #     html = zlib.decompress(content, -zlib.MAX_WBITS)
    # except zlib.error:
    #     html = gzip.decompress(content)
    html = gzip.decompress(content)
    proxies = REGEX_XICIDAILI.findall(html.decode())
    retval = []
    for proxy in proxies:
        retval.append((proxy[2].lower(), proxy[0], proxy[1]))

    return retval


def get_proxy_string(proxy_tuple):
    assert isinstance(proxy_tuple, tuple), '错误，必须是有三个元素的元组'
    assert len(proxy_tuple) == 3, '错误，必须是有三个元素的元组'
    scheme, ip, port = proxy_tuple
    return scheme.lower() + '://' + ip + ":" + port


def get_proxy_tuple(proxy_str):
    assert isinstance(proxy_str, str), '错误，必须是str'
    if 'http' not in proxy_str:
        proxy_str = 'http://' + proxy_str
    result = urlsplit(proxy_str)
    scheme = result.scheme
    ip = result.hostname
    port = result.port
    return scheme, ip, port


def verify_proxy(proxy_tuple):
    assert isinstance(proxy_tuple, tuple), '错误，必须是有三个元素的元组'
    assert len(proxy_tuple) == 3, '错误，必须是有三个元素的元组'

    scheme, ip, port = proxy_tuple
    proxy_support = urllib.request.ProxyHandler({'http': "{}:{}".format(ip, port)})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    try:
        test_url = 'http://httpbin.org/ip'
        req = urllib.request.Request(test_url)
        res = urllib.request.urlopen(req).read()
        print("********************* √ {}    -- {}".format(proxy_tuple, res))
    except Exception as e:
        print("******** ×, {} -- {}".format(proxy_tuple, e))


def verify_proxy_string(proxy_str):
    assert isinstance(proxy_str, str), '错误，必须是str'
    scheme, ip, port = get_proxy_tuple(proxy_str)
    proxy_support = urllib.request.ProxyHandler({'http': "{}:{}".format(ip, port)})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    try:
        test_url = 'http://httpbin.org/ip'
        req = urllib.request.Request(test_url)
        res = urllib.request.urlopen(req).read().decode()
        print("********************* √ {}    -- {}".format(proxy_str, res))
    except Exception as e:
        print("******** ×, {} -- {}".format(proxy_str, e))


def start_task():
    for item in PROXIES['66ip']:
        proxy = get_proxy_string(item)
        print(proxy)
        verify_proxy_string(proxy)


if __name__ == '__main__':
    verify_proxy_string('111.177.160.34:9999')
