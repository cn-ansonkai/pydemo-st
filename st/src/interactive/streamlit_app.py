# -*- coding: utf-8 -*-

from pyecharts.options import series_options
import streamlit as st
from pyecharts.charts import Pie
from pyecharts import options as opts
import streamlit.components.v1 as components
#from pyecharts.options import series_options as sopt

#import pandas as pd
#from streamlit_echarts import st_pyecharts
#from pyecharts.charts.basic_charts.bar import Bar

st.set_page_config(page_title='Demos Using Streamlit')
st.markdown(r"""## pyecharts with Streamlit and Streamlit-echarts
[pyecharts](https://github.com/pyecharts/pyecharts) is a python plotting library which uses [Echarts](https://github.com/ecomfe/echarts) as underlying implementation.
[Streamlit-echarts](https://github.com/andfanilo/streamlit-echarts) project combines Streamlit and Echarts.

### 示例列表
""")
series_data = [("紧急变更", 8),("重大变更", 0),("中型变更", 3),("小型变更", 259),("标准变更", 106)]
p = (
    Pie()
    .add(series_name='变更', data_pair=series_data, radius=["30%", "70%"])
    .set_global_opts(opts.TitleOpts(title="Pie——变更饼图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}：{c}"))
    .render_embed()
    )

#st_pyecharts(p)
components.html(p, width=1000, height=1000)
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
