# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年10月19日
@file:      main.py
"""

from flask import Flask
from web_service.index import index
from configparser import ConfigParser
from urllib.parse import quote

app = Flask(__name__, static_folder="", static_url_path="")

app.register_blueprint(index)

if __name__ == "__main__":
    config = ConfigParser()
    config.read("./config.ini", encoding="utf-8")
    host = quote(config.get("flask", "host"))
    port = quote(config.get("flask", "port"))
    app.run(host=host, port=port, debug=False)

