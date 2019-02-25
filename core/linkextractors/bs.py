# -*- coding: utf-8 -*-
# Author: FengQiMin<fengqimin@msn.com>
# Created on 2019-01-08 22:15:13
"""extractor

提取页面中的links和text等
"""
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from framework.core.linkextractors import BaseLinkExtractor
from framework.utils.href import HREF
from framework.utils.msic import remove_duplicates_from_list


class BSLinkExtractor(BaseLinkExtractor):
    """use bs4 extractor links

    """

    def __init__(self, tag='a', attr='href', process=None, **kwargs):
        BaseLinkExtractor.__init__(self, tag, attr, process, **kwargs)
        self.find_tag = tag if callable(tag) else lambda t: t.name == tag
        self.base_url = kwargs.get('base_url') or ''

    def _extract_links(self, response_text, response_encoding=None, response_url=None):
        # soup.find_all(lambda tag: tag.name == 'th' and tag.has_attr('class') and tag['class'] == ['common'])

        self.netloc = urlparse(self.base_url).netloc
        self.url = response_url
        self.text = response_text
        self.encoding = response_encoding or 'utf-8'
        soup = BeautifulSoup(response_text, 'lxml', from_encoding=response_encoding)

        _base_url = soup.base.get('href') if soup.base else ''
        # 确定base_url。优先级是初始化时指定的、从页面提取的、响应中的
        self.base_url = self.base_url or _base_url or response_url
        # self.base_url = urljoin(response_url, self.base_url)

        links = []

        for tag in soup.find_all(self.find_tag):
            # print(tag)
            if tag:
                url = tag.get(self.find_attr)
            else:
                continue

            if url:
                url = urljoin(self.base_url, url)
                link = HREF(url)
                if isinstance(tag.text, str):
                    # 利用字符串切割和合并，去除空白字符
                    link.text += ''.join(tag.text.split())
                links.append(link)
            else:
                pass
        return remove_duplicates_from_list(links)
