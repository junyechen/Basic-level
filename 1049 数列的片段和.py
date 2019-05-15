"""
给定一个正数数列，我们可以从中截取任意的连续的几个数，称为片段。例如，给定数列 { 0.1, 0.2, 0.3, 0.4 }，我们有 (0.1) (0.1, 0.2) (0.1, 0.2, 0.3) (0.1, 0.2, 0.3, 0.4) (0.2) (0.2, 0.3) (0.2, 0.3, 0.4) (0.3) (0.3, 0.4) (0.4) 这 10 个片段。

给定正整数数列，求出全部片段包含的所有的数之和。如本例中 10 个片段总和是 0.1 + 0.3 + 0.6 + 1.0 + 0.2 + 0.5 + 0.9 + 0.3 + 0.7 + 0.4 = 5.0。
输入格式：

输入第一行给出一个不超过 10​5​​ 的正整数 N，表示数列中数的个数，第二行给出 N 个不超过 1.0 的正数，是数列中的数，其间以空格分隔。
输出格式：

在一行中输出该序列所有片段包含的数之和，精确到小数点后 2 位。
输入样例：

4
0.1 0.2 0.3 0.4

输出样例：

5.00
"""

#####################################################################################################
"""
本题涉及到算法问题，将片段求和转化为每个数×出现次数的求和，每个数出现次数等同于左右两数列的组合数，当该数左边有m个数，则该数与其左列可形成m+1个数列，当该数右边有n个数，则该数与其右列可形成n+1个数列，该数出现次数即为左数列(m+1)×右数列(n+1)的组合数。
python3 下面几个例子都超时，查询网上代码发现并没有很大不同，只是用float替代eval，尝试替换后，后两个测试点均通过，说明明确数据类型转换的flaot比不明确的eval是要快很多133ms-->大于200ms
"""
#####################################################################################################

N = int(input())
number = [float(i) for i in input().split()]
weight = [(i + 1) * (N - i) for i in range(N)]
sum_ = sum([a * b for (a, b) in zip(number, weight)])
print('%.2f' % sum_)

'''
N = int(input())
number = [eval(i) for i in input().split()]
sum_ = 0
for i in range(N):
    sum_ += number[i] * (i + 1) * (N - i)
print('%.2f' % sum_)
'''

'''
N = int(input())
number = [eval(i) for i in input().split()]
weight = [(i + 1) * (N - i) for i in range(N)]
sum_ = 0
for i in range(N):
    sum_ += number[i] * weight[i]
print('%.2f' % sum_)
'''

'''
N = int(input())
number = [eval(i) for i in input().split()]
weight = [(i + 1) * (N - i) for i in range(N)]
sum_ = sum([a * b for (a, b) in zip(number, weight)])
print('%.2f' % sum_)
'''