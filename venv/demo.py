# coding=gbk
import time
ori=1568131200000/1000
time_tuple=time.localtime(ori)
t1=time.strftime("%Y-%m-%d",time_tuple)
#print(t1)
line='''

'''
import re#������ʽ�����ַ���
#m1=re.match(r'.*Data_netWorthTrend = (.*?);/*�ۼƾ�ֵ����*/var Data_ACWorthTrend.*',line3)
m1=line.split("Data_netWorthTrend =")[1].split(";/*�ۼƾ�ֵ����*/var Data_ACWorthTrend")[0]
if m1:
    print(m1)
else:
    print("nullll")
list = re.findall( '{"x":(.*?),"y":(.*?),"equityReturn":(.*?),"unitMoney":"(.*?)"}',m1)
num=1
print("end")

