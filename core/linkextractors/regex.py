# -*- coding: utf-8 -*-
import logging
import re
from html import unescape
from urllib.parse import urljoin

from framework.core.linkextractors import BaseLinkExtractor
from framework.utils.href import HREF
from framework.utils.msic import remove_duplicates_from_list

REGEX_BASE = re.compile(r'''(?im)<base href=["']?([^\s"'<>]+)["']?.+?/>''')

logger = logging.getLogger('_regex_link_extractor')


class RegexLinkExtractor(BaseLinkExtractor):
    """class for regex extractor

    """

    def __init__(self, tag, attr=None, process=None, **kwargs):
        super(RegexLinkExtractor, self).__init__(tag, attr, process, **kwargs)
        regex_link = re.compile(r'''(?im)href=["']?([^\s"'<>]+)["']?.+?>([^<>]*?)</a>''')
        regex_img = re.compile(
            r'''(?ims)<img.+?%s=["']?([^\s{}"'<>]+)["']?.*?(?:title)?=?["']?([^\s"'<>]*)["']?.*?/>''' % attr)
        regex_tag = re.compile(
            r'''(?ims)<%s.+?%s=["']?([^\s{}"'<>]+)["']?.*?.*?>([^<>]*?)''' % (tag, attr))
        self.find_tag = regex_link
        if tag == 'img':
            self.find_tag = regex_img

    def _extract_links(self, response_text, response_encoding=None, response_url=None):
        """利用re模块从data中解析出links，without blocking"""
        if isinstance(response_text, str):
            html = response_text
        elif isinstance(response_text, bytes):
            html = response_text.decode()
        else:
            return
        links = []
        # 提取links
        a_all = self.find_tag.findall(html)

        # 提取base_url
        try:
            _base_url = REGEX_BASE.findall(html)[0]
        except IndexError:
            _base_url = ''
        # 确定base_url。优先级是初始化时指定的、从页面提取的、响应中的
        self.base_url = self.base_url or _base_url or response_url

        logger.debug('base_url= %s' % self.base_url)
        for a in a_all:
            url, text = a
            url = urljoin(self.base_url, url)
            link = HREF(url)
            link.text = unescape(text)
            links.append(link)
        return remove_duplicates_from_list(links)

    # def _filter_tag(self, document):


