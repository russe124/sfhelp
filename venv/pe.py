import json

global peDict


def parseFile(code):
    f=open('d:/data/pe/'+code+'.txt',encoding='utf-8')
    content=f.read()#使用loads()方法，需要先读文件
    f.close()
    user_dic=json.loads(content)
    priceList=user_dic['price']
    pe_ttmList = user_dic['pe_ttm']
    dateList = user_dic['date']
    dict ={}
    peDict={}
    priceDict={}
    num=0

    #构建dict，往字典里添加对象
    for date in dateList:
        tup = (pe_ttmList[num],priceList[num])
        peDict[date]=pe_ttmList[num]
        priceDict[date] = priceList[num]
        num=num+1
    return peDict

def getGoodList(peDict,startTime,EndTime):
    list=[]
    for (key, value) in peDict.items():
        sign=calculateTime(key,startTime,EndTime)
        if sign==True:
            list.append(value)
    return list

def calculateTime(time,start,end):
    if time>=start and time<=end:
        return True
    else:
        return False

def calculatePercecnt(value,start='0000-00-00',end='9999-99-99'):
    global peDict
    goodList=getGoodList(peDict,start,end)
    #  p25 p50 p75
    print("good=",goodList)
    goodList.sort()
    print("sort=",goodList)
    sum=len(goodList)
    count=1
    p25=None
    p50 = None
    p75 = None
    rate=None
    print("sum=", sum)
    for v in goodList:
        if count==1:
            pmin=1
        pmax=v
        if p25 == None and count/sum>=0.25:
            p25=v
        if p50 == None and count/sum>=0.5:
            p50=v
        if p75 == None and count/sum>=0.75:
            p75=v
        if rate==None and value<=v:
            if count==1:
                rate='0%'
            else:
                rate=str(round(count/sum*100,2))+"%"
        count = count + 1
    if rate==None:
        rate='100%'

    print(pmin,'-',p25,'-',p50,'-',p75,'-',pmax,"=",rate)
import datetime
def standardData(value):
    # 将字符串转换为日期 string => datetime
    #d = datetime.datetime.strptime(t_str, '%Y-%m-%d')
    now = datetime.datetime.now()
    nows=now.strftime('%Y-%m-%d')
    d7 = (now + datetime.timedelta(days=-7)).strftime('%Y-%m-%d')
    d14 = (now + datetime.timedelta(days=-14)).strftime('%Y-%m-%d')
    d30 = (now + datetime.timedelta(days=-30)).strftime('%Y-%m-%d')
    d90 = (now + datetime.timedelta(days=-90)).strftime('%Y-%m-%d')
    d180 = (now + datetime.timedelta(days=-180)).strftime('%Y-%m-%d')
    y1 = (now + datetime.timedelta(days=-365)).strftime('%Y-%m-%d')
    y3 = (now + datetime.timedelta(days=-365)*3).strftime('%Y-%m-%d')
    y5 = (now + datetime.timedelta(days=-365)*5).strftime('%Y-%m-%d')
    print("\n7日百分线：")
    calculatePercecnt(value, d7,)
    print("\n14日百分线：")
    calculatePercecnt(value, d14,)
    print("\n30日百分线：")
    calculatePercecnt(value, d30,)
    print("\n90日百分线：")
    calculatePercecnt(value, d90,)
    print("\n180日百分线：" )
    calculatePercecnt(value, d180,)
    print("\n1年百分线：")
    calculatePercecnt(value,y1,)
    print("\n3年百分线：")
    calculatePercecnt(value, y3,)
    print("\n5年百分线：")
    calculatePercecnt(value, y5,)
    print("\n历史线：")
    calculatePercecnt(value,)

import requests
def SAreqNet(code):
    #code=str(icode)
    oricode=code
    if code[0]=='6':
        code='sh'+code
    else:
        code = 'sz' + code
    r0 = requests.get('https://eniu.com/chart/pea/' + code )
    ori = r0.text
    print(ori)
    path='d:/data/pe/'+oricode+'.txt'
    with  open(path, "w+")  as fo:
        fo.write(ori)
    fo.close()
    #txt文件中
#parseFile()
#calculateTime('2019-11-10','2019-11-02','2019-11-12')
#calculatePercecnt(35.05,'2019-08-13','2019-09-13')
#peDict=parseFile()
#calculatePercecnt(35.05,'1019-08-13','2019-09-13')
#standardData(35.05)

#step1 请求网络 step2从文件里读取
#code="002415" 海康威视
#code="601318" #中国平安
#code="000001" #平安银行
code="601319" #中国人保
#SAreqNet(code)#请求市盈率历史百分位函数
peDict=parseFile(code)
standardData(21.70)#打印结果