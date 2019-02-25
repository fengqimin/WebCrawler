# -*- coding: utf-8 -*-
"""downloaders

"""
import logging
import time

import aiohttp
import requests

from framework.utils.request import fake_headers

logger = logging.getLogger('download')

DATA_PATH = './data/'


class Downloader:
    """class Download"""

    def __init__(self, session=None, **kwargs):
        self.session = session if session else requests.Session()
        self.method = kwargs.get('method')
        self.headers = kwargs.get('headers') or fake_headers()
        self.retries = kwargs.get('retries') or 6
        self.timeout = kwargs.get('timeout') or 30
        self.stream = kwargs.get('stream', False)
        self.proxies = kwargs.get('proxies')

    def fetch(self, url, method=None, retries=6, timeout=30, stream=None, proxies=None, headers=None):
        """

        :param method:
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param headers: (optional)
        :param url:需要下载的地址
        :param timeout:referer_url How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read
            timeout) <timeouts>` tuple.
        :param proxies:(optional) Dictionary mapping protocol to the URL of the proxy.
        :param retries:(optional) How many times to retry
        :return:Response
        """
        logger.info('Start download %s...' % url)

        _retries = retries if retries else self.retries
        _timeout = timeout if timeout else self.timeout
        _stream = stream if stream is not None else self.stream
        _proxies = proxies if proxies else self.proxies
        _headers = headers if headers else self.headers
        _method = method if method else 'GET'

        logger.debug('headers:%s' % _headers)

        while _retries:
            try:
                return requests.request(url=url, method=_method,
                                        proxies=_proxies, timeout=_timeout, stream=_stream, headers=_headers)
            except IOError:
                time.sleep(5)
                _retries = _retries - 1

    def handle_request(self, request: requests.Request):
        # req = requests.Request(url=)
        pass

    def handle_response(self, response):
        pass

    def handle_exception(self, _exception):
        pass


class AsyncDownloader:
    """利用 aiohttp 实现异步请求
    对aiohttp进行了简单的封装
    """

    def __init__(self, loop=None, **kwargs):
        self.responses = []
        self.loop = loop
        self.method = kwargs.get('method', 'GET')
        self.headers = kwargs.get('headers')
        self.retries = kwargs.get('retries', 6)
        self.timeout = kwargs.get('timeout', 30)
        self.stream = kwargs.get('stream', False)
        self.proxy = kwargs.get('proxy')

    async def fetch(self, url, method=None, retries=6, timeout=30, proxy=None, headers=None):
        logger.debug('Start download %s...' % url)

        def handle_request(request):
            # req = requests.Request(url=)
            return request

        def handle_response(response):
            return response

        _retries = retries if retries else self.retries
        _timeout = timeout if timeout else self.timeout
        _proxy = proxy if proxy else self.proxy
        _headers = headers if headers else self.headers
        _method = method if method else self.method

        logger.debug('headers:%s' % _headers)
        async with aiohttp.ClientSession() as s:
            async with s.request(url=url, method=_method,
                                 proxy=_proxy, timeout=_timeout, headers=_headers) as resp:
                assert resp.status == 200, '%s, %s' % (resp.status, url)
                await resp.read()
        return handle_response(resp)

    async def download_func(self, url):
        d = AsyncDownloader(retries=5)
        resp = await d.fetch(url)
        self.responses.append(resp)

    def handle_exception(self, _exception):
        pass


def test():
    pass


if __name__ == '__main__':
    test()
