#ĳ��������˿��ղ飬�õ���ȫ���������ա�������д�������ҳ��������곤����������ˡ�

#����ȷ��ÿ����������ڶ��ǺϷ��ģ�����һ���Ǻ���ġ���������֪����û�г��� 200 ������ˣ��������� 2014 �� 9 �� 6 �գ����Գ��� 200 ������պ�δ���������ն��ǲ�����ģ�Ӧ�ñ����˵���

#�����ʽ��

#�����ڵ�һ�и��������� N��ȡֵ��(0,10
#?5
#?? ]����� N �У�ÿ�и��� 1 ���˵��������ɲ����� 5 ��Ӣ����ĸ��ɵ��ַ��������Լ��� yyyy/mm/dd������/��/�գ���ʽ���������ա���Ŀ��֤���곤�����������û�в��С�

#�����ʽ��

#��һ����˳�������Ч���յĸ��������곤�˺��������˵�����������Կո�ָ���

#����������

#5
#John 2001/05/12
#Tom 1814/09/06
#Ann 2121/01/30
#James 1814/09/05
#Steve 1967/11/20
#���������

#3 Tom John

##########################################################################
#���������յ�������ʽ������ֱ�ӽ����ַ�����С�Ƚϣ�������ת�������ڸ�ʽ
#ע����Դ����������ݶ������䲻�����
#python��ʱ�޷����
    #������������C++д�Ĵ��룬ǰ�������Ծ�Ϊ2ms�����һ��Ϊ125ms
    #��pythonǰ�������Ծ���20+ms����˱ض���ʱ
##########################################################################

#import datetime

#N=int(input())
#data=[]
#today=datetime.datetime(year=2014,month=9,day=6)
#oldday=datetime.datetime(year=1814,month=9,day=6)
#young=[0,0,datetime.timedelta(days=201*365)]
#old=[0,0,datetime.timedelta(days=-1)]
#for i in range(N):
#    line=input().split()
#    line.append(datetime.datetime.strptime(line[1],"%Y/%m/%d"))
#    if line[2]>today or line[2]<oldday:
#        pass
#    else:
#        data.append(line)
#        delta=today-data[-1][2]
#        if delta<young[2]:
#            young=data[-1]
#            young[2]=delta
#        if delta>old[2]:
#            old=data[-1]
#            old[2]=delta
#print(len(data),old[0],young[0])

N=int(input())
data=[]
today="2014/09/06"
oldday="1814/09/06"
young=[0,"1814/09/05"]
old=[0,"2014/09/07"]
for i in range(N):
    line=input().split()
    if line[1]>today or line[1]<oldday:
        pass
    else:
        data.append(line)
        if line[1]>young[1]:
            young=line
        if line[1]<old[1]:
            old=line
if len(data)==0:
    print(0)
else:
    print(len(data),old[0],young[0])