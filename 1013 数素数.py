#令 P​i​​ 表示第 i 个素数。现任给两个正整数 M≤N≤10​4​​，请输出 P​M​​ 到 P​N​​ 的所有素数。
#输入格式：

#输入在一行中给出 M 和 N，其间以空格分隔。
#输出格式：

#输出从 P​M​​ 到 P​N​​ 的所有素数，每 10 个数字占 1 行，其间以空格分隔，但行末不得有多余空格。
#输入样例：

#5 27

#输出样例：

#11 13 17 19 23 29 31 37 41 43
#47 53 59 61 67 71 73 79 83 89
#97 101 103

#用python实现素数方法，基本绕不开超时这个问题，目前的办法只有埃拉托色尼筛法可以再python语境下完成时间要求
#不同于之前的1007，为了得到完整地数表，可以先用常规素数方法算出第1000个素数是多少，之后以其为常量建立表筛选出素数

mn = str(input())
mn = mn.split()
m = int(mn[0])
n = int(mn[1])

#####  算得第10000个质数为104729，该程序段完成历史使命
#primes = [2]
#total = 1
#num = 3
#while total < n:
#    i = 0
#    flag = True
#    while primes[i] * primes[i] <= num:
#        if num % primes[i] == 0:
#            flag = False
#            break
#        i = i + 1
#    if flag:
#        primes.append(num)
#        total = total + 1
#    num = num + 2
##########

maxium = 104729
num = [0] * (maxium+1)  #避免溢出
total = 1
primes = [2]
i = 3
while total < n:
    if num[i] == 0:
        primes.append(i)
        total = total + 1
        j = i * i
        while j < maxium:
            num[j] = 1
            j = j + i * 2
    i = i + 2
i = m
primes = list(map(str,primes))
while i < n - 10:
    print(' '.join(primes[i - 1:i + 9]))
    i = i + 10
print(' '.join(primes[i - 1:n]))

