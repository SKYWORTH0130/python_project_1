from flask import Flask, render_template, request
import pandas as pd
import plotly as py
from plotly.graph_objs import Scatter,Layout,Data
import plotly.graph_objs as go
import cufflinks as cf
from pyecharts import options as opts
from pyecharts.charts import Geo,Map,Timeline,Page
from pyecharts.globals import ChartType, SymbolType,ThemeType

app = Flask(__name__)

df = pd.read_csv("D:/A/学习/Python学习/上交作业/期末项目/期末/Area _ first vaccination rate.csv", encoding='utf-8',)
df2 = pd.read_csv("D:/A/学习/Python学习/上交作业/期末项目/期末/Area _ first vaccination rate.csv", encoding='utf-8', index_col="region")
df3 = df2.loc[:,::-1]
df5 = pd.read_csv("D:/A/学习/Python学习/上交作业/期末项目/期末/2000-2018Measles Incidence.csv",encoding = 'utf8')
df7 = pd.read_csv("D:/A/学习/Python学习/上交作业/期末项目/期末/Reported measles cases.csv",encoding = 'utf8')
dfc = pd.read_csv("D:/A/学习/Python学习/上交作业/期末项目/期末/Country _ first vaccination rate.csv",encoding = "utf8")

dfq = pd.read_csv("D:/A/学习/Python学习/上交作业/期末项目/期末/Cumulative measles deaths averted by vaccination.csv",encoding = 'utf8')
dfb = dfq.drop(6)
regions_available_loaded= list(df.region)
cf.set_config_file(offline =True,theme = "ggplot")
py.offline.init_notebook_mode()

def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2009,2019):
        map0 = (
            Map()
            .add(
                "接种率",list (zip(list(df.Country),list(df["{}".format(i)]))),"world",is_map_symbol_show = False
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}全球各国第一支疫苗接种率".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=100,min_=35),
            )
        )
        tl.add(map0, "{}".format(i))
    return tl

def bar_base1() -> Bar:
    c = (
        Bar()
        .add_xaxis(list(df7.region))
        .add_yaxis("2000", list(df7['2000']))
        .add_yaxis("2018", list(df7['2018']))
        .set_global_opts(title_opts=opts.TitleOpts(title="00年与18年麻疹病例报道对比", subtitle=""))
    )
    return c

def bar_base2() -> Bar:
    ww= (
        Bar()
        .add_xaxis(list(df5.region))
        .add_yaxis("2000", list(df5['2000']))
        .add_yaxis("2018", list(df5['2018']))
        .set_global_opts(title_opts=opts.TitleOpts(title="00年与18年麻疹发病率对比", subtitle=""))
    )
    return ww

tab = Tab()
tab.add(bar_base1(), "麻疹病例数量报道")
tab.add(bar_base2(), "麻疹发病率")

def timeline_map1() -> Timeline:
    tl = Timeline()
    for i in range(2011,2020):
        map0 = (
            Map()
            .add(
                "案例数量",list (zip(list(dfv.Country),list(dfv["{}".format(i)]))),"world",is_map_symbol_show = False
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年全球各国麻疹案例".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=6000,min_=1),
            )
        )
        tl.add(map0, "{}".format(i))
    return tl

def data_select() -> 'html':
    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region)  ## 检查用户输入, 在后台

    dfs = df.query("region=='{}'".format(the_region))  ## 使用df.query()方法. 按用户交互输入the_region过滤

    data_str = dfs.to_html()  # 数据产出dfs, 完成互动过滤呢

    # 使用iplot 做bar圖
    fig = df.iplot(kind="bar", x="region", y="2018", asFigure=True)
    py.offline.plot(fig, filename="1111.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("1111.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    regions_available = regions_available_loaded  # 下拉选单有内容
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           the_select_region=regions_available,
                           )

def try_1() -> 'html':
    Global = go.Scatter(
        x=[x for x in df3.columns.values],
        y=df3.loc["Global"].values,
        name="全球")

    Africa = go.Scatter(
        x=[x for x in df3.columns.values],
        y=df3.loc["Africa"].values,
        name="非洲")

    Americas = go.Scatter(
        x=[x for x in df3.columns.values],
        y=df3.loc["Americas"].values,
        name="美洲")

    South_East_Asia = go.Scatter(
        x=[x for x in df3.columns.values],
        y=df3.loc["South-East Asia"].values,
        name="东南亚")

    Europe = go.Scatter(
        x=[x for x in df3.columns.values],
        y=df3.loc["Europe"].values,
        name="欧洲")

    Eastern_Mediterranean = go.Scatter(
        x=[x for x in df3.columns.values],
        y=df3.loc["Eastern Mediterranean"].values,
        name="地中海东部")

    Western_Pacific = go.Scatter(
        x=[x for x in df3.columns.values],
        y=df3.loc["Western Pacific"].values,
        name="西太平洋")

    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([dict(count=5,
                                                                   label="5年",
                                                                   step="year",
                                                                   stepmode="backward"),
                                                              dict(count=10,
                                                                   label="10年",
                                                                   step="year",
                                                                   stepmode="backward"),
                                                              dict(count=20,
                                                                   label="20年",
                                                                   step="year",
                                                                   stepmode="backward"),
                                                              dict(count=30,
                                                                   label="30年",
                                                                   step="year",
                                                                   stepmode="backward"),
                                                              dict(step="all")
                                                              ])
                                                ),
                             rangeslider=dict(bgcolor="#FFF3D6"),
                             title="年份"
                             ),
                  yaxis=dict(title="疫苗接种率"),
                  title="全球各地区疫苗接种率"
                  )

    fig = dict(data=[Global, Africa, Americas, South_East_Asia, Europe, Eastern_Mediterranean, Western_Pacific],
               layout=layout)

    py.offline.plot(fig, filename="全球各地区疫苗接种率.html", auto_open=False)
    with open("全球各地区疫苗接种率.html", encoding="utf8", mode="r") as c:
        plot_all = "".join(c.readlines())

    return render_template('results2.html',
                           the_plot_all=plot_all)


if __name__ == "__main__":
    app.run()