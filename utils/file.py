# -*- coding: utf-8 -*-
import os.path


def list_files(path, ext='.htm'):
    """遍历文件夹下的文件，并返回文件路径列表
     :param ext: Filename Extension
     :param path:
     :return:
     """
    if not os.path.exists(path):
        return None
    _path_list = []
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        # 如果是文件, and 扩展名为htm*
        if os.path.isfile(sub_path) and (ext in sub_path):
            # 将文件名加入到列表中
            _path_list.append(sub_path)

    return _path_list


def list_dirs(path):
    """遍历文件夹下的文件夹，并返回文件夹路径列表
    :param path:
    :return:
    """
    if not os.path.exists(path):
        os.mkdir(path)
    _path_list = []
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        # 如果是文件夹
        if os.path.isdir(sub_path):
            _path_list.append(sub_path)
    return _path_list


def file_already_fetched(path, content_size):
    """比较字节大小，验证文件文件是否已经完全获取  """
    # 
    if os.path.exists(path):
        file_size = os.path.getsize(path)
    else:
        return False

    if file_size >= content_size:
        return True
    else:
        return False


def normalize_path(path, invalid_chars='[\\/:*?"<>|]', new=''):
    """规范化文件和目录路径
      """
    # _isdir = os.path.isdir(path)
    # print(_isdir)
    _drive, _path = os.path.splitdrive(path)
    for ch in invalid_chars:
        _path = _path.replace(ch, new)
    return os.path.join(_drive, _path)


def title2path(base_path, html_title, sep=' - ', maxsplit=1):
    """根据页面标题，形成目录名

        :param maxsplit: 最大分割次数
        :param html_title:html页面标题
        :param base_path: 基础路径
        :param sep: 分隔符
        :return:
    """

    path = []
    html_title = normalize_path(html_title)
    _path = base_path
    for p in html_title.rsplit(sep, maxsplit):
        path.append(p.strip())

    try:
        while maxsplit > -1:
            _path = os.path.join(_path, path[maxsplit])
            maxsplit -= 1
        return _path
    except IndexError:
        return ''


if __name__ == '__main__':
    print(title2path("E:\\downloads\\Picture\\.adult\\HKPic", '西田藍 - 明星寫真區'))
