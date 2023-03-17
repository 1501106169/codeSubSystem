# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年10月19日
@file:      call_docker.py
"""

from sys import stderr, stdout
from traceback import print_list
from click import command
import docker
from configparser import ConfigParser
from urllib.parse import quote

# 读取配置文件
config = ConfigParser()
config.read("./config.ini", encoding="utf-8")

# 读取镜像数据文件夹路径配置
image_test_data_dir = quote(config.get("imagePath", "testDataDir"))
# 镜像算法文件夹路径配置
image_algorithm_dir = quote(config.get("imagePath", "algorithmDir"))

def run_images(test_data_dir: str, algorithm_dir: str) -> str:
    """
    创建容器执行算法, 获得结果
    :param test_data_dir: str
        测试数据文件夹路径
    :param algorithm_dir: str
        算法文件夹路径
    :return str
    """
    docker_client = docker.from_env()
    container = docker_client.containers.run(
        "scheduler-image-v1.1:latest", 
        detach=True, 
        remove=True, 
        tty=True, 
        volumes=[test_data_dir + ":" + image_test_data_dir, algorithm_dir + ":" + image_algorithm_dir],
        command="java -jar /usr/local/scheduler/scheduler.jar")
    out = "".join([bt.decode("utf-8") for bt in container.logs(stdout=True, stderr=True, stream=True)])
    return out


if __name__ == "__main__":
    test_data_dir = quote(config.get("localPath", "testDataDir"))
    algorithm_dir = quote(config.get("localPath", "algorithmDir"))
    print(run_images(test_data_dir=test_data_dir, algorithm_dir=algorithm_dir))

