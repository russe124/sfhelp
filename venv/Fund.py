import requests #导入requests，然后就可以为所欲为了
import re#正则表达式处理字符串
#http://baijiahao.baidu.com/s?id=1599992188940440730&wfr=spider&for=pc
import time
#发送get请求 请求单个基金的今日数据
def SAsingleJJ(code):
 #   code='501019'
    r0 = requests.get("http://fundgz.1234567.com.cn/js/"+code+".js?jzrq=2019-09-10")
    #print(r0.text)

    #line='jsonpgz({"fundcode":"'+code+'","name":"富国文体健康股票","jzrq":"2019-09-11","dwjz":"1.1140","gsz":"1.1155","gszzl":"0.13","gztime":"2019-09-12 15:00"},{"fundcode":"001186","name":"富国文体健康股票","jzrq":"2019-09-11","dwjz":"1.1140","gsz":"1.1155","gszzl":"0.13","gztime":"2019-09-12 15:00"});'
    line=r0.text
    path='d:/data/'+code+'.csv'
    #fo = open("d:/data/"+code+".csv", "w")#全量写入
    fo = open(path,"a")#追加写入
    it = re.finditer( '{"fundcode":"(.*?)","name":"(.*?)","jzrq":"(.*?)","dwjz":"(.*?)","gsz":"(.*?)","gszzl":"(.*?)","gztime":"(.*?)"',line,re.M)
    count = len(open(path, 'r').readlines())
    if count==0:
        fo.write('fundcode,name,jzrq,dwjz,gsz,gszzl,gztime\n')
    #fo.readline
    #
    for match in it:
        print (match.group())
        for pp in match.groups():
            print(pp, end=',')
            fo.write(pp+',')
        fo.write('\n')
    # 关闭打开的文件
    fo.close()
    print("\nfinished")

def formatTime(oristr):
    ori = float(oristr) / 1000
    time_tuple = time.localtime(ori)
    t1 = time.strftime("%Y-%m-%d", time_tuple)
    return str(t1)

#请求单个基金的历史数据和详细数据
#目前只做了净值的提取
def SAsingleDetail(code):
        r0 = requests.get('http://fund.eastmoney.com/pingzhongdata/'+code+'.js')
        ori=r0.text
        line = ori.split("Data_netWorthTrend =")[1].split(";/*累计净值走势*/var Data_ACWorthTrend")[0]
        print(line)
        num=1
        path='d:/data/JJ-'+code+'.csv'
         # 追加写入
        print(path)
        it = re.finditer( '{"x":(.*?),"y":(.*?),"equityReturn":(.*?),"unitMoney":"(.*?)"}',line,re.M)

        with  open(path, "a+")  as fo:
            count = len(open(path, 'r').readlines())
            if count == 0:
                fo.write('x,y,equityReturn,unitMoney\n')
            for match in it:
                firstField = 1
                for pp in match.groups():
                    if firstField==1:
                        pp=formatTime(pp)
                        firstField=firstField+1
                    print(pp, end=',')
                    fo.write(pp + ',')
                fo.write('\n')
        # 关闭打开的文件
        fo.close()
        print("\nfinished")

def reqFundAll(code,url,path,regx,title,sub_start,sub_end):

    r0 = requests.get(url)
    ori=r0.text
    line = ori.split(sub_start)[1].split(sub_end)[0]
    print(line)
    #fo = open("d:/data/"+code+".csv", "w")#全量写入
    with  open(path, "a+")  as fo:#追加写入
        it = re.finditer( regx,line,re.M)
        count = len(open(path, 'r').readlines())
        if count==0:
            fo.write(title+'\n')

        for match in it:
            print (match.group())
            for pp in match.groups():
                print(pp, end=',')
                fo.write(pp+',')
            fo.write('\n')
        # 关闭打开的文件
    fo.close()
    print("\nfinished")
import configparser

def readConf():
    '''
    cf.read(filename)：读取文件内容
    cf.sections()：得到所有的section，并且以列表形式返回
    cf.options(section)：得到section下所有的option
    cf.items(option)：得到该section所有的键值对
    cf.get(section,option)：得到section中option的值，返回string类型的结果
    cf.getint(section,option)：得到section中option的值，返回int类型的结果
    ():元组
    []:数组
    {}:字典
    '''
    cf = configparser.ConfigParser()
    cf.read("conf.ini")
    host = cf.get("datatest", "host")
    print(host)
    print(cf.options("myFundList"))
    print(cf.items("myFundList")[0][0])

def changeGoldData(code):

        r0 = requests.get("http://fundgz.1234567.com.cn/js/" + code + ".js")
        dri=r0.text



#读取单个基金单日表现
#singleJJ('501019')
#读取单个基金详情
#singleDetail('001186')
#格式化时间字符串方法
#print(formatTime(float("1434988800000")))

#查询所有基金
#reqFundAll(code="all",url="http://fund.eastmoney.com/js/fundcode_search.js",path="d:/data/FundAll.csv",regx='\["(.*?)","(.*?)","(.*?)","(.*?)","(.*?)"\]',title='编码,简称,全程,类型,拼音',sub_start="var r = ",sub_end=";")
#读取配置文件
readConf()