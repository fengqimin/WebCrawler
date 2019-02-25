# -*- coding: utf-8 -*-
from urllib.parse import urlsplit, unquote_plus
from html import unescape
from framework.utils.url import normalize_url


class HREF(object):
    """HREF objects represent an extracted href by the LinkExtractor.

    Copyright (c) Scrapy developers.
    """

    __slots__ = ['url', 'fragments', 'text', 'nofollow', 'mimetype', 'store']

    def __init__(self,
                 url: str,
                 text='',
                 nofollow=False,
                 mimetype='text/html'
                 ):
        """
        :param url:str
        :param text:str，url的文本描述，<a href=url>text</a>
        :param nofollow:str,nofollow标签是由谷歌领头创新的一个"反垃圾链接"的标签,
                用于指示搜索引擎不要追踪（即抓取）网页上的带有nofollow属性的任何出站链接，
                以减少垃圾链接的分散网站权重！
        :param mimetype:str, 规定目标 URL 的 MIME 类型。仅在 href 属性存在时使用。
        """

        if not isinstance(url, str):
            raise TypeError('URL must be str objects, got %s' % url.__class__.__name__)
        # 转义
        url = unescape(url)
        self.url = normalize_url(url)
        self.text = text
        self.nofollow = nofollow
        self.mimetype = mimetype
        self.fragments = urlsplit(unquote_plus(url)).fragment
        self.store = None

    def __eq__(self, other):
        return self.url == other.url

    def __repr__(self):
        return 'Link(url=%r, text=%r, fragments=%r, nofollow=%r, mimetype=%r, store=%r)' % \
               (self.url, self.text, self.fragments, self.nofollow, self.mimetype, self.store)

    def __hash__(self):
        """在set，frozenset，dict这三种数据结构中，都要求键值key是可hash的，因此重写了哈希方法"""
        return hash(self.url) ^ hash(self.text) ^ hash(self.fragments) ^ hash(self.nofollow) ^ hash(self.mimetype)
