# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年10月19日
@file:      index.py
"""

from flask import Blueprint, request
from flask_cors import cross_origin
from configparser import ConfigParser
from urllib.parse import quote
from sys_call.write_file import write_algorithm_file
from sys_call.call_docker import run_images

config = ConfigParser()
config.read("./config.ini", encoding="utf-8")

index = Blueprint("demo", __name__)

@index.route("/", methods=["post"])
@cross_origin()
def run_algorithm():
    data = request.json
    code_type = data.get("codeType")
    code = data.get("code")
    algorithm_dir = quote(config.get("localPath", "algorithmDir"))
    if write_algorithm_file(dir_path=algorithm_dir, content=code) is False:
        return "error"
    test_data_dir = quote(config.get("localPath", "testDataDir"))
    res = run_images(test_data_dir=test_data_dir, algorithm_dir=algorithm_dir)
    return res

