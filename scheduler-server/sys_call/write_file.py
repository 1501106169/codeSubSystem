# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年10月19日
@file:      write_file.py
"""

import os
from configparser import ConfigParser
from urllib.parse import quote

config = ConfigParser()
config.read("./config.ini", encoding="utf-8")

file_name = quote(config.get("fileName", "algorithmFileName"))

def write_algorithm_file(dir_path: str, content: str) -> bool:
    """
    向指定的算法文件夹写入算法源代码
    :param dirPath: str
        文件夹路径
    :param content: str
        算法源代码
    :return: bool
    """
    file_path = os.path.join(dir_path, file_name)
    with open(file=file_path, mode="w", encoding="utf-8") as fd:
        fd.write(content)
    return True

