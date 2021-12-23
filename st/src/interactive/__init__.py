# -*- coding: utf-8 -*-
from pywebio.output import *

async def pyecharts_localdraw():
    """在PyWebIO中使用 pyecharts 进行数据可视化示例。"""
    put_markdown(r"""## pyecharts和PyWebIO

    PyWebIO 支持输出使用 pyecharts 库创建的图表。

    """
    , lstrip=4)