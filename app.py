from flask import Flask, render_template, request, escape
import pandas as pd
import plotly as py
from plotly.graph_objs import Scatter,Layout,Data
import plotly.graph_objs as go
import cufflinks as cf
from pyecharts import options as opts
from pyecharts.charts import Geo,Map,Timeline,Page
from pyecharts.globals import ChartType, SymbolType,ThemeType

app = Flask(__name__)

df = pd.read_csv("2.csv", encoding='utf-8',)
df2 = pd.read_csv("2.csv", encoding='utf-8', index_col="region")
df3 = df2.loc[:,::-1]
df5 = pd.read_csv("1.csv",encoding = 'utf8')
df7 = pd.read_csv("5.csv",encoding = 'utf8')
dfc = pd.read_csv("3.csv",encoding = "utf8")

dfq = pd.read_csv("4.csv",encoding = 'utf8')
dfb = dfq.drop(6)
regions_available_loaded= list(df.region)
cf.set_config_file(offline =True,theme = "ggplot")
py.offline.init_notebook_mode()
app = Flask(__name__)

@app.route('/')
def home_page() -> 'html':
    """连接主页"""
    return render_template('index.html',
	                       the_title = '欢迎来到我们组的网站')

@app.route('/one')
def one():
    return render_template('00年和18年对比.html')
	
@app.route('/two')
def two():
    return render_template('222.html')
	
@app.route('/three')
def three():
    return render_template('1111.html')
	
@app.route('/four')
def four():
    return render_template('2018年各地区接种疫苗避免的麻疹死亡比例.html')

@app.route('/five')
def five():
    return render_template('render.html')
	
@app.route('/six')
def six():
    return render_template('地图_全球各国麻疹案例.html')

@app.route('/seven')
def seven():
    return render_template('全球各地区疫苗接种率.html')

if __name__ == '__main__':
    app.run(debug=True)