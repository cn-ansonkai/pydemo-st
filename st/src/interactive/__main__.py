# -*- coding: utf-8 -*-
from pywebio import start_server

from . import pyecharts_localdraw

if __name__ == '__main__':
    start_server(pyecharts_localdraw, port=8085, debug=True, auto_open_webbrowser=False)