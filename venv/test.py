import tushare as ts
d = ts.get_tick_data('601318',date='2017-06-26')
#print(d)
e = ts.get_hist_data('601318',start='2017-06-23',end='2017-06-26')
#print(e)
df = ts.get_hist_data('000875')
#df.to_csv('d:/data/000875.csv')


d = ts.get_hist_data('600519',start='2019-08-12',end='2019-09-12')
#d.to_csv('d:/data/600519.csv')
#print(d)
ss=ts.get_stock_basics()
d = ts.get_hist_data('000001',start='2019-08-12',end='2019-09-12')
d = ts.get_hist_data('sh',start='2019-08-12',end='2019-09-12')
#d.to_csv('d:/data/sh.csv')
a1=d.head(10)
#print(a1)

import tushare  as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#sz=a1.sort_index(axis=0, ascending=True) #对index进行升序排列
#sz_return=sz[['p_change']] #选取涨跌幅数据
#train=sz_return[0:255] #划分训练集
#test=sz_return[255:]   #测试集
#对训练集与测试集分别做趋势图
#plt.figure(figsize=(10,5))
#train['p_change'].plot()
#plt.legend(loc='best')
#plt.show()
#plt.figure(figsize=(10,5))
#test['p_change'].plot(c='r')
#plt.legend(loc='best')
#plt.show()

# help(ts.get_hist_data) 了解参数
code='600519'
dh = ts.get_hist_data(code)
df = dh.sort_values(by='date')
df.reset_index(inplace=True)
# 取样 2019年以后的数据
d2 = df[df['date'] > '2019-01-01']
print(d2.head())
d2.index = pd.to_datetime(d2.date)

# 画股价走势图
fig, axes = plt.subplots(2, 1)
d2[['close', 'ma5', 'ma10', 'ma20']].plot(ax=axes[0], grid=True, title=code)
# 画股票成交量图
#d2[['volume']].plot(ax=axes[1], grid=True)
#plt.show()
#https://tushare.pro/document/1?doc_id=40
ts.set_token('412a06b413114c8e56aa4ac2b56a4b76caa08c5d8d216ea845987680')
pro = ts.pro_api()
#df = pro.fund_nav(ts_code='165509.SZ')
#print(df)

