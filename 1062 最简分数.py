"""
一个分数一般写成两个整数相除的形式：N/M，其中 M 不为0。最简分数是指分子和分母没有公约数的分数表示形式。

现给定两个不相等的正分数 N​1​​/M​1​​ 和 N​2​​/M​2​​，要求你按从小到大的顺序列出它们之间分母为 K 的最简分数。
输入格式：

输入在一行中按 N/M 的格式给出两个正分数，随后是一个正整数分母 K，其间以空格分隔。题目保证给出的所有整数都不超过 1000。
输出格式：

在一行中按 N/M 的格式列出两个给定分数之间分母为 K 的所有最简分数，按从小到大的顺序，其间以 1 个空格分隔。行首尾不得有多余空格。题目保证至少有 1 个输出。
输入样例：

7/18 13/20 12

输出样例：

5/12 7/12
"""

###################################################
"""
这道题最大公约数算法，也是可行的；
原来的做法求出素数表，然后求出分母K的质因数表，然后得到与分母K最大约分的数值表，结果总是报错，换用了最大公约数算法后也还是报错，最后发现定边界值出现问题，不能将等号囊括进去
此外，还需注意要求将两个分数先求大小！
"""
###################################################

def gcd(k,K):
    while k%K!=0:
        temp = k%K
        k = K
        K = temp
    return K

N, M, K = [eval(i) for i in input().split()]
if N > M:
    temp = N
    N = M
    M = temp
i = int(K * N)
if i / K <= N:
    i += 1
j = int(K * M)
if j / K >= M:
    j -= 1
out = ''
for k in range(i,j + 1):
    if gcd(k,K) == 1:
        out += str(k) + r'/' + str(K) + ' '
print(out[:-1])




###############################################

###############################################

"""
#生成素数表
prime = [1] * 1001
prime[0], prime[1] = 0, 0
for i in range(4,1001,2):
    prime[i] = 0
for i in range(3,1001,2):
    if prime[i] == 1:
        p = i + i * 2
        while p < 1001:
            prime[p] = 0
            p += i * 2
temp = []
for i in range(2,1001):
    if prime[i] == 1:
        temp.append(i)
prime = temp
#输入
N, M, K = [eval(i) for i in input().split()]
if N > M:
    temp = N
    N = M
    M = temp
prime_ = []
#获得分母质因数表
if K in prime:
    prime_ = [K]
else:
    for i in prime:
        if K % i == 0:
            prime_.append(i)
        if i * i > K:
            break
poss = [1] * 1001
poss[0] = 0
for i in prime_:
    p = i
    while p < 1001:
        poss[p] = 0
        p += i
i = int(K * N)
if i / K <= N:
    i += 1
j = int(K * M)
if j / K >= M:
    j -= 1
out = ''
for k in range(i,j + 1):
    if poss[k] == 1:
        out += str(k) + r'/' + str(K) + ' '
print(out[:-1])
"""