# -*- coding: utf-8 -*-
import hashlib
import re
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode

from framework.utils.file import normalize_path

__all__ = ["STORED", "CRAWLED", "SEEN", "URL_CRAWL_STATUS", "is_duplicate_url",
           "replace_url_host", "normalize_url", "url2filename", "url2fn_hash"]

REGEX_TAG_A_HREF = re.compile(r'''(?i)href=["']([^\s"'<>]+)''')
REGEX_TITLE = re.compile(r'<title>(.+)</title>')

# ---------------------------------------------------------------------------#
#   URL爬取状态
# ---------------------------------------------------------------------------#
STORED = 30  # URL指向的资源已经存储
CRAWLED = 20  # URL已经爬取
SEEN = 10  # URL还未爬取
UNKNOWN = 0  # 状态未知，预留，实际无意义

URL_CRAWL_STATUS = {
    UNKNOWN: 'UNKNOWN',
    SEEN: 'SEEN',
    CRAWLED: 'CRAWLED',
    STORED: 'STORED',
}


def url2filename(url, base_url=None, _filter=''):
    """把url转换成符合windows规范的文件名
    """
    scheme, netloc, path, params, query, fragment = urlparse(url)
    if base_url and netloc in base_url:
        _filename = '_'.join(path.strip('/').split('/'))
    else:
        # http://www.wailian.work/images/2018/06/05/15.gif
        _filename = netloc + '_' + '_'.join(path.strip('/').split('/'))
    return normalize_path(_filename).replace(_filter, '')


def url2fn_hash(url) -> str:
    path = urlparse(url).path
    hash_ = hashlib.sha1()
    hash_.update(url.encode())
    file_ext = path.split('.')[-1]
    if file_ext == path:
        file_ext = 'html'
    hash_fn = hash_.hexdigest() + '.' + file_ext

    return hash_fn


def normalize_url(url: str, keep_blank_values=True, allow_fragments=False) -> str:
    """规范化url
    -排序查询
    -去除查询空值，如果keep_blank_value=False
    -去除fragment，如果keep_fragment=False
    """
    # https://www.baidu.com/baidu?wd=anonicalize&tn=monline_4_dg&ie=utf-8
    # https://www.baidu.com/baidu?ie=utf-8&tn=monline_4_dg&wd=anonicalize
    (scheme, netloc, path, params, query, fragment) = urlparse(url)
    # 去除查询空值，如果keep_blank_value=False
    qsl = parse_qsl(query, keep_blank_values)
    # 排序查询
    query = urlencode(sorted(qsl))
    # 去除fragment，如果keep_fragment=False
    fragment = fragment if allow_fragments else ''
    url = urlunparse((scheme, netloc, path, params, query, fragment))

    return url


def is_duplicate_url(url, urls):
    """判断url是否重复
    determine if duplicate
    :param url:str
    :param urls:
    :return:
    """
    return urlparse(url).path in urls


def replace_url_host(url: str, new):
    host_old = urlparse(url).hostname
    url = url.replace(host_old, new, 1)
    return url


if __name__ == '__main__':
    URL = 'https://www.baidu.com/baidu?wd=data+uri&tn=hello&ie=utf-8#12'
    print(normalize_url(URL))
