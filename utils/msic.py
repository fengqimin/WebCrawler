# encoding: utf-8
import hashlib
import json
from urllib.parse import urlparse

# __always_supported = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
#                       'blake2b', 'blake2s',
#                       'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
#                       'shake_128', 'shake_256')
hash_func = {
    'md5': hashlib.md5(),
    'sha1': hashlib.sha1(),
    'blake2b': hashlib.blake2b(),
    'blake2s': hashlib.blake2s(),
    'sha3_224': hashlib.sha3_224(),
    'sha3_256': hashlib.sha3_256(),
    'sha3_512': hashlib.sha3_512(),
}


def read_html(html_file, encoding='utf-8'):
    with open(html_file, 'r', encoding=encoding) as fp:
        data = fp.read()
    return data


def hash_id(string: str, algorithms='sha1'):
    _id = hash_func[algorithms]
    _id.update(string.encode())
    return _id.hexdigest()


def remove_duplicates_from_list(_list, key=lambda x: x):
    """利用集合实现高效的列表去重复项，并确保列表内各元素的顺序不变
    :return: list,
    """
    key = key if callable(key) else lambda x: x
    _scanned_set = set()
    result = []
    for item in _list:
        scanned_key = key(item)
        if scanned_key in _scanned_set:
            continue
        _scanned_set.add(scanned_key)
        result.append(item)
    return result


def init_json(in_file='../data/hkpic_link.txt', to_file='../data/Hkpic_requested_urls.json'):
    d = dict()
    d['http://hkpic.net'] = []
    with open(in_file, 'r', encoding='utf-8') as fp:
        for data in fp.readlines():
            url = data.split(',')[0]
            path = urlparse(url).path
            d['http://hkpic.net'].append(path)
    with open(to_file, 'w') as fp:
        json.dump(d, fp)


def load_json(json_file: str):
    """从文件中载入json
    """
    if isinstance(json_file, str):
        file = json_file
        with open(file, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            return data
    else:
        return None


def dump_json(data, file):
    """导出已经被爬取url的json

    :param data:已经被请求url的列表
    :param file:json文件
    :return:
    """
    with open(file, 'w', encoding='utf-8') as fp:
        json.dump(data, fp)


def load_requested_urls(file_or_list):
    """载入已经被爬取ulr的json
    """
    if isinstance(file_or_list, str):
        file = file_or_list
        with open(file, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
    else:
        data = file_or_list

    data = set(data)

    return data


def dump_requested_url(done_urls, file):
    """导出已经被爬取url的json

    :param done_urls:已经被请求url的列表
    :param file:json文件
    :return:
    """
    if isinstance(done_urls, set):
        done_urls = list(done_urls)

    if file:
        with open(file, 'w', encoding='utf-8') as fp:
            json.dump(done_urls, fp)


def json2db(json_file, db_file=r'D:\My Projects\Python\WebCrawler\copy_hkpic.db'):
    import sqlite3
    import hashlib
    status = 'SUCCESS'

    with open(json_file, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    db_conn = sqlite3.connect(db_file)
    cur = db_conn.cursor()
    # print(len(data))
    data = set(data)
    # print(len(data))

    for url in data:
        col_id = hashlib.sha1()
        col_id.update(url.encode())
        col_id.update(status.encode())
        col_url = url
        col_status = status
        column = (col_id.hexdigest(), col_url, col_status)
        print(column)
        cur.execute('INSERT INTO seen_urls VALUES (?,?,?)', column)
    cur.close()
    db_conn.commit()
    db_conn.close()


class ProgressBar(object):
    """进度表
    作者：微微寒
    链接：https://www.zhihu.com/question/41132103/answer/93438156
    来源：知乎
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def __init__(self, count=0.0, chunk_size=1.0, total=100.0, title="", run_status="", fin_status="", unit='',
                 sep='/'):
        """初始化

        :param title: total=content_size
        :param count:
        :param run_status: run_status="正在下载"
        :param fin_status: fin_status="下载完成"
        :param total:远程文件的大小
        :param unit: 单位"KB"
        :param sep:分割线
        :param chunk_size: 数据块的大小
        """
        super(ProgressBar, self).__init__()
        self.info = "[%s] %.2f%% %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def _get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (
            self.title, 100 * self.count / self.total, self.count / self.chunk_size, self.unit, self.seq,
            self.total / self.chunk_size,
            self.unit)
        return _info

    def refresh(self, count=1, status=None):
        """refresh progress bar

        :param count:
        :param status:
        :return:
        """
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self._get_info(), end=end_str)


if __name__ == '__main__':
    pass
