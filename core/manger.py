# -*- coding: utf-8 -*-
# Author: FengQiMin<fengqimin@msn.com>
# Created on 2019-01-08 00:15:13
"""URL Manager

负责待爬取URL和已爬取URL的管理，实现URL去重，可以考虑使用内存、数据库或缓存数据库方式实现，最简单的方式使用set。
"""
import asyncio
import sqlite3
from collections import namedtuple
from urllib.parse import *

from config.hkpicconfig import THREAD_URL
from framework.utils.url import *
from framework.utils.href import HREF
from framework.utils.logformatter import log_formatter
from framework.utils.msic import (hash_id,
                                  remove_duplicates_from_list)

logger = log_formatter(__name__)

FetchStatistic = namedtuple('FetchStatistic',
                            ['url',
                             'next_url',
                             'status',
                             'exception',
                             'size',
                             'content_type',
                             'encoding',
                             'num_urls',
                             'num_new_urls'])


class Manager(object):
    """base class for spider manager

    """

    def __int__(self, root_urls: list, work_queue, exclude=None, strict=True, **kwargs):
        self.root_urls = root_urls
        self.work_queue = work_queue or asyncio.Queue()
        self.exclude = exclude

        # ------------------------------
        # 从kwargs中读取参数
        # ------------------------------
        # 使用sqlite3数据库记录日志
        self.db_file: str = kwargs.get('db_file')
        self.db_conn = sqlite3.connect(self.db_file) if self.db_file else None
        self.cursor = self.db_conn.cursor() if self.db_conn else None
        # 允许抓取的host
        self.allowed_hosts: list = kwargs.get('allow_hosts') or []
        self.base_url = kwargs.get('base_url') or ''
        self.json_file = kwargs.get('json_file')

        # 等待爬取的urls列表，不使用set的目的是为了保持顺序
        self.todo_urls = []
        # 已经爬取的urls列表
        self.done_urls = set()
        # 已经见过的url集合（全集，包括done_urls，差集为todo_urls集合）
        self.seen_urls = set()

    def add_link(self, link: HREF):
        """加入到待下载队列中，同时加入到seen集合中, without blocking

        :param link:
        :return:
        """
        if link.url in self.seen_urls or not self.url_allowed(link.url):
            return

        logger.debug('adding %r' % link)
        self.seen_urls.add(link.url)
        self.work_queue.put_nowait(link)

        # 保存到数据库中
        if self.cursor:
            status = URL_CRAWL_STATUS[SEEN]
            _id = hash_id(link.url + status)
            try:
                self.cursor.execute('INSERT INTO seen_urls VALUES (?,?,?)', (_id, link.url, status))
            except sqlite3.Error as e:
                logger.debug(e)

    def add_links(self, links: list):
        for link in links:
            self.add_link(link)

    def process_link(self, link: HREF):
        # 替换缩略图为原始文件
        if not self.url_allowed(link.url):
            return None
        url = link.url.replace('jpg.thumb.jpg', 'jpg')
        (scheme, netloc, path, params, query, fragment) = urlparse(url)

        # url转换
        # 'forum.php?# mod=viewthread&tid=5363742&highlight=%E9%AD%94%E5%B9%BB%E7%A6%8F%E5%88%A9
        # ->'thread-5363742-1-1.html'
        if query:
            # parse_qs-> {'mod': ['viewthread'], 'tid': ['3850510'], 'highlight': ['魔幻福利']}
            result = parse_qs(query)
            tid = result.get('tid')
            if tid:
                url = THREAD_URL.format(id=tid[0])
        url = urljoin(self.base_url, url)
        link.url = url
        return link

    def process_links(self, links: list):
        # URL去重
        links = remove_duplicates_from_list(links, key=lambda x: x.url)
        retval = []
        for link in links:
            link = self.process_link(link)
            if link:
                retval.append(link)
        return retval

    def url_allowed(self, url: str) -> bool:
        # 排除
        if self.exclude and url.find(self.exclude):
            return False
        parts = urlsplit(url)
        # scheme
        if parts.scheme not in ('http', 'https', 'ftp'):
            return False
        # hostname
        if parts.hostname not in self.allowed_hosts:
            return False
        return True

    def record_statistic(self, fetch_statistic):
        """Record the FetchStatistic for completed / failed URL."""
        self.done_urls.add(fetch_statistic)


if __name__ == '__main__':
    l1 = list()
    l1.append(None)
    print(l1)
