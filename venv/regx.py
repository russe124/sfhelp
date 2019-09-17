import re#正则表达式处理字符串

def regx1():
    line='["000001","HXCZHH","华夏成长混合","混合型","HUAXIACHENGZHANGHUNHE"],["000002","HXCZHH","华夏成长混合(后端)","混合型","HUAXIACHENGZHANGHUNHE"]'
    it = re.finditer(r'\["000001","HXCZHH","华夏成长混合","混合型","HUAXIACHENGZHANGHUNHE"\]', line)
    for match in it:
     print("ss",match)
    for pp in match.groups():
        print("ww"+pp, end=',')

def regx2():
    str=jsonpgz({"fundcode":"002611","name":"鍗氭椂榛勯噾ETF鑱旀帴C","jzrq":"2019-09-12","dwjz":"1.1887","gsz":"1.1859","gszzl":"-0.23","gztime":"2019-09-17 02:29"});
    it = re.finditer(r'str=jsonpgz({(.*?))', line)