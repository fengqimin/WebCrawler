# -*- coding: utf-8 -*-
import logging


def config_logger(log_name, log_file=None,
                  level=logging.DEBUG,
                  file_handler_level=logging.INFO,
                  stream_handler_level=logging.DEBUG):
    """设置日志格式

    :param level:
    :param log_name:
    :param log_file:
    :param file_handler_level:
    :param stream_handler_level:
    :return:
    """
    _logger = logging.getLogger(log_name)

    if log_file:
        # 创建文件处理器
        file_handler = logging.FileHandler(filename=log_file, encoding='utf-8')
        file_handler.setLevel(file_handler_level)

        # 定义输出格式
        file_formatter = logging.Formatter('%(lineno)4d - %(asctime)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        # 将创建的文件和流处理器添加logger中
        _logger.addHandler(file_handler)

    # 创建流输出处理器，用于输出
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_handler_level)

    # 定义输出格式
    stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_formatter)

    # 将创建的文件和流处理器添加logger中
    _logger.addHandler(stream_handler)

    _logger.setLevel(level)
    return _logger


def log_formatter(log_name, log_file=None, log_level=logging.INFO):
    _logger = logging.getLogger(log_name)

    # 创建文件处理器
    if log_file:
        file_handler = logging.FileHandler(filename=log_file, encoding='utf-8')
        file_handler.setLevel(log_level)
        # 定义输出格式
        file_formatter = logging.Formatter('%(lineno)4d - %(asctime)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        # 将创建的文件和流处理器添加logger中
        _logger.addHandler(file_handler)

    # 创建流处理器，用于控制台输出
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_formatter)

    _logger.addHandler(stream_handler)

    _logger.setLevel(logging.DEBUG)
    return _logger
