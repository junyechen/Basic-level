# 让我们定义d​n​​为：d​n​​=p​n+1​​−p​n​​，其中p​i​​是第i个素数。显然有d​1​​=1，且对于n>1有d​n​​是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。

# 现给定任意正整数N(<10​5​​)，请计算不超过N的满足猜想的素数对的个数。
# 输入格式:

# 输入在一行给出正整数N。
# 输出格式:

# 在一行中输出不超过N的满足猜想的素数对的个数。
# 输入样例:

# 20

# 输出样例:

# 4

#import time
#time_start=time.time()

#import math

#n = int(input())
#prime = [3]
#d = 0

#prime_suspect = 5
#prime_last_1 = 3
#prime_last_2 = 3
#while prime_suspect <= n:
#    isPrime = True
#    sqrt = int(math.sqrt(prime_suspect))
#    for i in prime:
#        if i > sqrt:
#            break
#        if prime_suspect % i == 0:
#            isPrime = False
#            break
#    if isPrime:
#        prime_last_1 = prime_last_2
#        prime_last_2 = prime_suspect
#        prime.append(prime_suspect)
#        prime_suspect += 2
#        if prime_last_2-prime_last_1 == 2:
#            d += 1
#    else:
#        prime_suspect += 2
#print(d)

#time_end=time.time()
#print('totally cost',time_end-time_start)

##生成素数列表方法
n = int(input())
prime = [0] * 100000

Primes = [2,3]

i = 3
d = 0
while i <= n:
    if prime[i] == 1:
        i += 2
    else:
        Primes.append(i)
        p = i * i
        while p < n:
            prime[p] = 1
            p += i * 2
        i += 2
        if Primes[-1] - Primes[-2] == 2:
            d += 1

print(d)