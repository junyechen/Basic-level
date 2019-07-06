"""
2004 年 7 月，谷歌在硅谷的 101 号公路边竖立了一块巨大的广告牌（如下图）用于招聘。内容超级简单，就是一个以 .com 结尾的网址，而前面的网址是一个 10 位素数，这个素数是自然常数 e 中最早出现的 10 位连续数字。能找出这个素数的人，就可以通过访问谷歌的这个网站进入招聘流程的下一步。

prime.jpg

自然常数 e 是一个著名的超越数，前面若干位写出来是这样的：e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921... 其中粗体标出的 10 位数就是答案。

本题要求你编程解决一个更通用的问题：从任一给定的长度为 L 的数字中，找出最早出现的 K 位连续数字所组成的素数。
输入格式：

输入在第一行给出 2 个正整数，分别是 L（不超过 1000 的正整数，为数字长度）和 K（小于 10 的正整数）。接下来一行给出一个长度为 L 的正整数 N。
输出格式：

在一行中输出 N 中最早出现的 K 位连续数字所组成的素数。如果这样的素数不存在，则输出 404。注意，原始数字中的前导零也计算在位数之内。例如在 200236 中找 4 位素数，0023 算是解；但第一位 2 不能被当成 0002 输出，因为在原始数字中不存在这个 2 的前导零。
输入样例 1：

20 5
23654987725541023819

输出样例 1：

49877

输入样例 2：

10 3
2468024680

输出样例 2：

404
"""

################################################
"""
一开始想建立素数表，结果占用空间太大，运行速度非常慢
查看网上的资源，发现只要最简单的每个数判断是否为素数即可
    在这过程中出现一点小问题：
        在判断1和2是没有单独考虑，导致2个测试点没有通过
"""
################################################

def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3,int(n ** 0.5),2):
        if n % i == 0:
            return False
    return True

L, K = [int(i) for i in input().split()]
N = input()
for i in range(L - K + 1):
    if isprime(int(N[i:i + K])):
        print(N[i:i + K])
        exit(0)
print("404")

###############################################
"""
prime = [1] * 1000000000
prime[0], prime[1] = 0, 0
for i in range(4,1000000000,2):
    prime[i] = 0
for i in range(3,31623,2):
    temp = i
    if prime[i] == 1:
        temp += i * 2
        while temp < 1000000000:
            prime[temp] = 0
            temp += i * 2
L, K = [int(i) for i in input().split()]
N = input()
for i in range(L - K + 1):
    if prime[int(N[i:i + K])] == 1:
        print(N[i:i + K])
        exit(0)
print("404")
"""
###############################################