# -*- coding: utf-8 -*-
from urllib.parse import urljoin

from lxml import etree

from framework.core.linkextractors import BaseLinkExtractor
from framework.utils.href import HREF


class LxmlLinkExtractor(BaseLinkExtractor):
    """base class for extractor,base_url可以为'',否则必须是绝对url
    """

    def __init__(self, selector, attr, process=None, **kwargs):
        super(LxmlLinkExtractor, self).__init__(selector, attr, process, **kwargs)
        self.selector = selector

    def _extract_links(self, response_text, response_encoding=None, response_url=''):
        """提取链接的具体实现，需要重载"""
        if isinstance(response_text, bytes):
            response_text = response_text.decode(response_encoding)
        html = etree.HTML(response_text)
        # 提取base_url
        _base_url = html.base
        # 确定base_url。优先级是初始化时指定的、从页面提取的、响应中的
        base_url = self.base_url or _base_url or response_url
        # base_url = urljoin(response_url, base_url)

        elements = html.cssselect(self.selector)
        _retval = []
        for el in elements:
            url = el.get(self.find_attr)
            if url:
                url = urljoin(base_url, url)
                text = el.text
                link = HREF(url, text)
                _retval.append(link)
        return _retval

    def _process_links(self, links):
        """处理链接的具体实现，需要重载"""
        return self.process(links)

    def _handler_expectation(self, expectation):
        pass

    def _filter_tags(self, document: etree.Element):
        for element in document.iter():
            if not self.find_tag(element.tag):
                pass
