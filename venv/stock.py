import tushare as ts

#提取数据有一些问题，还在查询中
def SAwhiteHorse():
    '''
（1）每股收益在0.25元以上 股票列表 esp
（2）每股净资产值3.00元为底线  股票列表 bvps
（3）净资产收益率10%以上 业绩报告（主表） roe
（4）平均市盈率为40倍 实时行情 per
（5）净利润增长率30%以上 股票列表 npr
（6）主营业务收入增长率30%以上 股票列表 rev
    :return:
  '''
    # http://blog.sina.com.cn/s/blog_9aecc9930102xf97.html
    # 用tushare筛选出具有高送转潜力的股票
    # 基本面数据
    basic = ts.get_stock_basics()  # 股票列表
    print("step1 获取基本面数据")
    # 行情和市值数据
    hq = ts.get_today_all()  # 实时行情
    print("step2 获取行情市值数据")
    # 业绩报告数据（2016年3季度）
    re = ts.get_report_data(2019, 2)  # 业绩报告
    print("step2 业绩报告数据（2016年3季度）")
    # 把空值设置为0
    re.fillna(0)
    # 当前股价，如果停牌则设置当前价格为上一交易日价格
    hq['trade'] = hq.apply(lambda x: x.settlement if x.trade == 0 else x.trade, axis=1)
    # 分别获取流通股本 总股本 每股公积金 每股收益
    basedata = basic[['esp', 'bvps', 'rev', 'pb']]
    # 获取净资产收益率(%)
    redata = re[['code', 'roe']]
    # 设置re数据 code 为index列
    redata = redata.set_index('code')
    # 选取股票代码 名称 当前价格 总市值 流通市值
    hqdata = hq[['code', 'name', 'trade']]
    # 设置行情数据 code 为index列
    hqdata = hqdata.set_index('code')
    # 合并表格
    data1 = basedata.merge(redata, left_index=True, right_index=True)
    data = data1.merge(hqdata, left_index=True, right_index=True)
    # 讲总市值和流通市值换成亿元单位
    #  data['mktcap'] = data['mktcap'] / 10000
    #   data['nmc'] = data['nmc'] / 10000
    # 设置参数和过滤值

    # 每股收益>=5毛
    eps = data.esp >= 0.25
    bvps = data.bvps >= 3
    pb = data.pb >= 20
    #  npr=data.npr >=20
    # ROE在3%以上
    roe = data.roe >= 10

    # 取并集结果
    allcrit = pb & eps & bvps & roe
    selected = data[allcrit]
    # q1['code'] = selected['code'].astype(str)
    #  finalRes=q1.drop_duplicates(['code'])
    selected.to_csv('d:/data/2019-02-white.csv')

import datetime
# 实时行情 ts.get_today_all() 一次性获取当前交易所有股票的行情数据（如果是节假日，即为上一交易日，结果显示速度取决于网速）
#获取当天的行情数据
def SAgetAllTodayData():
    d=ts.get_today_all()
    now = datetime.datetime.now()
    nows=now.strftime('%Y-%m-%d')
    d.to_csv('d:/data/'+nows+'-all.csv')

#股票列表 ts.get_stock_basics() 获取沪深上市公司基本情况
def getAllStockList():
    d=ts.get_stock_basics()
    d.to_csv('d:/data/2019-09-12-bacicAll.csv')

#按季度获取利润数据（报表是1个累加的过程）
def SAgetProfit(year, month):
 #   print(str(year)+"-"+str(month))
    d=ts.get_report_data(year,month)
    d.to_csv('d:/data/get_report_data-'+str(year)+"-"+str(month)+'.csv')

#用tushare筛选出具有高送转潜力的股票
# http://blog.sina.com.cn/s/blog_9aecc9930102xf97.html
#市值<=100亿
#每股收益>=5毛
#每股公积金>=5
#市值<=100亿
#ROE在3%以上
def SAgetPotential():
    # 基本面数据
    basic = ts.get_stock_basics()#股票列表
    print("step1 获取基本面数据")
    # 行情和市值数据
    hq = ts.get_today_all()#实时行情
    print("step2 获取行情市值数据")
    # 业绩报告数据（2016年3季度）
    re = ts.get_report_data(2018, 4)#业绩报告
    print("step2 业绩报告数据（2016年3季度）")
    # 把空值设置为0
    re.fillna(0)
    # 当前股价，如果停牌则设置当前价格为上一交易日价格
    hq['trade'] = hq.apply(lambda x: x.settlement if x.trade == 0 else x.trade, axis=1)
    # 分别获取流通股本 总股本 每股公积金 每股收益
    basedata = basic[['outstanding', 'totals', 'reservedPerShare', 'esp']]
    # 获取净资产收益率(%)
    redata = re[['code', 'roe']]
    # 设置re数据 code 为index列
    redata = redata.set_index('code')
    # 选取股票代码 名称 当前价格 总市值 流通市值
    hqdata = hq[['code', 'name', 'trade', 'mktcap', 'nmc']]
    # 设置行情数据 code 为index列
    hqdata = hqdata.set_index('code')
    # 合并表格
    data1 = basedata.merge(redata, left_index=True, right_index=True)
    data = data1.merge(hqdata, left_index=True, right_index=True)
    # 讲总市值和流通市值换成亿元单位
    data['mktcap'] = data['mktcap'] / 10000
    data['nmc'] = data['nmc'] / 10000
    # 设置参数和过滤值
    # 每股公积金>=5
    res = data.reservedPerShare >= 5
    # 流通股本<=3亿
    out = data.outstanding <= 30000
    # 每股收益>=5毛
    eps = data.esp >= 0.5
    # 市值<=100亿
    mktcap = data.mktcap <= 100
    # ROE在3%以上
    roe = data.roe >= 3
    # 取并集结果
    allcrit = res & out & eps & mktcap & roe
    selected = data[allcrit]
   # q1['code'] = selected['code'].astype(str)
  #  finalRes=q1.drop_duplicates(['code'])
    selected.to_csv('d:/data/2018-04-potential-sin.csv')

#getAllTodayData()
#getProfit(2019,2)
#getPotential()
#getWhite()
getAllTodayData()
