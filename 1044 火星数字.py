"""
火星人是以 13 进制计数的：

    地球人的 0 被火星人称为 tret。
    地球人数字 1 到 12 的火星文分别为：jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec。
    火星人将进位以后的 12 个高位数字分别称为：tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou。

例如地球人的数字 29 翻译成火星文就是 hel mar；而火星文 elo nov 对应地球数字 115。为了方便交流，请你编写程序实现地球和火星数字之间的互译。
输入格式：

输入第一行给出一个正整数 N（<100），随后 N 行，每行给出一个 [0, 169) 区间内的数字 —— 或者是地球文，或者是火星文。
输出格式：

对应输入的每一行，在一行中输出翻译后的另一种语言的数字。
输入样例：

4
29
5
elo nov
tam

输出样例：

hel mar
may
115
13
"""

"""
本题的问题在于火星文不按照位数输出，若为13的整数倍，则只输出高位，不输出末位0，即13=tam 而不是tam tret
"""

d_h_l = ('tret','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec')
d_h_h = ('','tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou')
h_d = {'tret':0,'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jly':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12,'tam':13, 'hel':26, 'maa':39, 'huh':52, 'tou':65, 'kes':78, 'hei':91, 'elo':104, 'syy':117, 'lok':130, 'mer':143, 'jou':156}
N = int(input())
for i in range(N):
    temp = input()
    if temp.isdigit():
        if int(temp) // 13 != 0:
            if int(temp) % 13 != 0:
                print(d_h_h[int(temp) // 13],d_h_l[int(temp) % 13])
            else:
                print(d_h_h[int(temp) // 13])
        else:
            print(d_h_l[int(temp)])
    else:
        temp = temp.split()
        try:
            print(h_d[temp[0]] + h_d[temp[1]])
        except:
            print(h_d[temp[0]])