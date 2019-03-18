#大家应该都会玩“锤子剪刀布”的游戏：两人同时给出手势，胜负规则如图所示：

#FigCJB.jpg

#现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。
#输入格式：

#输入第 1 行给出正整数 N（≤10​5​​），即双方交锋的次数。随后 N 行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。C 代表“锤子”、J 代表“剪刀”、B 代表“布”，第 1 个字母代表甲方，第 2 个代表乙方，中间有 1 个空格。
#输出格式：

#输出第 1、2 行分别给出甲、乙的胜、平、负次数，数字间以 1 个空格分隔。第 3 行给出两个字母，分别代表甲、乙获胜次数最多的手势，中间有 1 个空格。如果解不唯一，则输出按字母序最小的解。
#输入样例：

#10
#C J
#J B
#C B
#B B
#B C
#C C
#C B
#J B
#B C
#J J

#输出样例：

#5 3 2
#2 3 5
#B B

##########################
#超时
#relation = {('C','C'):'T',
#          ('J','J'):'T',
#          ('B','B'):'T',
#          ('C','J'):'W',
#          ('C','B'):'L',
#          ('J','C'):'L',
#          ('J','B'):'W',
#          ('B','C'):'W',
#          ('B','J'):'L'
#          }
#A = {'W':0,'T':0,'L':0}
#win = {
#    ('W','C'):0,
#    ('W','J'):0,
#    ('W','B'):0,
#    ('L','C'):0,   #实际布B赢
#    ('L','J'):0,   #实际锤C赢
#    ('L','B'):0    #实际剪J赢
#    }
#Bwin = {'C':'B',
#      'J':'C',
#      'B':'J'
#      }
#times = int(input())
#while times > 0:
#    result = input().split()
#    A[relation[result[0],result[1]]] += 1
#    try:
#        win[relation[result[0],result[1]],result[0]] += 1
#    except:
#        pass
#    finally:
#        times -= 1

#print(A['W'],A['T'],A['L'])
#print(A['L'],A['T'],A['W'])
#Awin = sorted(win.items(),key=lambda x:(x[0][0],x[1],-ord(x[0][1])),reverse=True)
#Awin_ = sorted(Awin[3:],key=lambda x:(x[1],-abs(ord(x[0][1]) - 70.3)),reverse=True)
#print(Awin[0][0][1],Bwin[Awin_[0][0][1]])
############################

############################
#仍旧超时
#挪用了网上C++的代码，前5个测试点为2ms，最后一个测试点31ms
#而python的代码，前5个测试点为22ms，最后一个测试点超时
relation = {('C','C'):'T',
          ('J','J'):'T',
          ('B','B'):'T',
          ('C','J'):'W',
          ('C','B'):'L',
          ('J','C'):'L',
          ('J','B'):'W',
          ('B','C'):'W',
          ('B','J'):'L'
          }
A = {'W':0,'T':0,'L':0}
Awin = {
    ('W','C'):0,
    ('W','J'):0,
    ('W','B'):0,
    }
Bwin = {
    ('L','B'):0,
    ('L','C'):0,
    ('L','J'):0
    }

times = int(input())
while times > 0:
    result = input().split()
    WL = relation[result[0],result[1]]
    A[WL] += 1
    if WL == 'W':
        Awin[WL,result[0]] += 1
    elif WL == 'L':
        Bwin[WL,result[1]] += 1
    times -= 1
print(A['W'],A['T'],A['L'])
print(A['L'],A['T'],A['W'])
Awin = sorted(Awin.items(),key=lambda x:(x[1],-ord(x[0][1])),reverse=True)
Bwin = sorted(Bwin.items(),key=lambda x:(x[1],-ord(x[0][1])),reverse=True)
print(Awin[0][0][1],Bwin[0][0][1])