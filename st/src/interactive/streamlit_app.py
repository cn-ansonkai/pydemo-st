# -*- coding: utf-8 -*-

#from pyecharts.options import series_options
from os import name
import streamlit as st
import streamlit.components.v1 as components
from pyecharts.charts import Pie, Bar
from pyecharts import options as opts
#from pyecharts.options import series_options as sopt

#import pandas as pd
#from streamlit_echarts import st_pyecharts
#from pyecharts.charts.basic_charts.bar import Bar

# 渐变色的javascript
color_js = """
            new echarts.graphic.LinearGradient(
                                0,
                                1,
                                0,
                                0,
                                [{offset: 0, color: '#00008B'},
                                 {offset: 1, color: '#DA70D6'}],
                                false)
           """

series_data = [("紧急变更", 8),("重大变更", 0),("中型变更", 3),("小型变更", 259),("标准变更", 106)]

# ECharts 属性来配置itemstyle
p = (
    Pie()
    .add(series_name='变更', data_pair=series_data, radius=["30%", "70%"])
    .set_global_opts(opts.TitleOpts(title="Pie——变更饼图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"), itemstyle_opts={
        'shadowBlur': 10,   # 光晕
        'shadowColor': 'rgba(0, 0, 0, 0.5)',  # 阴影颜色
        'shadowOffsetY': 5,  # 阴影偏移量——Y方向
        'shadowOffsetX': 5,  # 阴影偏移量——X方向
        })
    .render_embed()
    )

series_data_x = ["紧急变更", "重大变更", "中型变更", "小型变更", "标准变更"]
series_data_y = [
    opts.BarItem(name="紧急变更", value=8), 
    opts.BarItem(name="重大变更", value=0), 
    opts.BarItem(name="中型变更", value=3),
    opts.BarItem(name="小型变更", value=259),
    opts.BarItem(name="标准变更", value=106)
]

bb = (
    Bar()
    .add_xaxis(series_data_x)
    .add_yaxis("", series_data_y, itemstyle_opts=opts.ItemStyleOpts())
)

st.set_page_config(page_title='Demos Using Streamlit')
st.markdown(r"""## pyecharts with Streamlit and Streamlit-echarts
[pyecharts](https://github.com/pyecharts/pyecharts) is a python plotting library which uses [ECharts](https://github.com/ecomfe/echarts) as underlying implementation.
### 示例列表
""")

code_to_display = """
series_data = [("紧急变更", 8),("重大变更", 0),("中型变更", 3),("小型变更", 259),("标准变更", 106)]
p = (
    Pie()
    .add(series_name='变更', data_pair=series_data, radius=["30%", "70%"])
    .set_global_opts(opts.TitleOpts(title="Pie——变更饼图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render_embed()
    )
"""
components.html(p, width=1000, height=500)

with st.expander("Show Source Code"):
    st.code(code_to_display)

# st.markdown(r"""第二个示例

# ---
# """)

# components.html(p2, width=1000, height=500)
# st.title('Demo Using Streamlit')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# load_placeholder = st.empty()
# load_placeholder.text('Loading data...')
#with load_placeholder.container():
#    data_load_state = st.text('Loading data...')
# data = load_data(1000)
# load_placeholder.text("Done! (Cached)")
# load_placeholder.empty()

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# Some number in the range 0-23
#
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#
#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)
