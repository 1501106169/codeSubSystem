# -*- coding: utf-8 -*-
"""
@author:    hanyg
@date:      22年11月02日
@file:      tronado_server.py
"""

from main import app
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=80)
    IOLoop.instance().start()
