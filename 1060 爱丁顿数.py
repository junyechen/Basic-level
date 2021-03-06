"""
英国天文学家爱丁顿很喜欢骑车。据说他为了炫耀自己的骑车功力，还定义了一个“爱丁顿数” E ，即满足有 E 天骑车超过 E 英里的最大整数 E。据说爱丁顿自己的 E 等于87。

现给定某人 N 天的骑车距离，请你算出对应的爱丁顿数 E（≤N）。
输入格式：

输入第一行给出一个正整数 N (≤10​5​​)，即连续骑车的天数；第二行给出 N 个非负整数，代表每天的骑车距离。
输出格式：

在一行中给出 N 天的爱丁顿数。
输入样例：

10
6 7 6 9 3 10 8 2 7 8

输出样例：

6
"""

###############################################
"""
本题一开始的方法，测试点3过不去，但是总感觉程序没有问题；
查看网上和我类似的解法，他是额外用了E；但感觉i和E并没有区别；
最后突然意识到，如果所有数据都大于总天数，那么我这个输出的i就比E小了1！
最后测试数据发现，果然如此！很多事不能想当然啊！注意边界情况的测试！
"""
###############################################

N = int(input())
data = [int(i) for i in input().split()]
data.sort(reverse=True)
E = 0
for i in range(N):
    if data[i] > E + 1:
        E += 1
print(i)

"""
N = int(input())
data = [int(i) for i in input().split()]
data.sort(reverse=True)
for i in range(N):
    if data[i] <= i + 1:
        break
print(i)
"""