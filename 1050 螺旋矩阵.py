"""
本题要求将给定的 N 个正整数按非递增的顺序，填入“螺旋矩阵”。所谓“螺旋矩阵”，是指从左上角第 1 个格子开始，按顺时针螺旋方向填充。要求矩阵的规模为 m 行 n 列，满足条件：m×n 等于 N；m≥n；且 m−n 取所有可能值中的最小值。
输入格式：

输入在第 1 行中给出一个正整数 N，第 2 行给出 N 个待填充的正整数。所有数字不超过 10​4​​，相邻数字以空格分隔。
输出格式：

输出螺旋矩阵。每行 n 个数字，共 m 行。相邻数字以 1 个空格分隔，行末不得有多余空格。
输入样例：

12
37 76 20 98 76 42 53 95 60 81 58 93

输出样例：

98 95 93
42 37 81
53 20 76
58 60 76
"""

##########################################################
"""
1. 审题：非递增顺序输出
2. list.sort(reverse=True)
3. 二维列表建立方法：[[0 for i in range(n)] for j in range(m)]
"""
##########################################################
N = int(input())
number = [int(i) for i in input().split()]
number.sort(reverse=True)
n = int(N ** 0.5)
for i in range(n,0,-1):
    if N / i == int(N / i):
        n = i
        m = int(N / n)
        break
matrix = [[0 for i in range(n)] for j in range(m)]
top, bottom, left, right = 0, m - 1, 0, n - 1
index, i, j = 0, 0, 0
while index < N:
    try:
        while j <= right:
            matrix[i][j] = number[index]
            j += 1
            index += 1
        top += 1
        j -= 1
        i += 1
        while i <= bottom:
            matrix[i][j] = number[index]
            i += 1
            index += 1
        right -= 1
        i -= 1
        j -= 1
        while j >= left:
            matrix[i][j] = number[index]
            j -= 1
            index += 1
        bottom -= 1
        j += 1
        i -= 1
        while i >= top:
            matrix[i][j] = number[index]
            i -= 1
            index += 1
        left += 1
        i += 1
        j += 1
    except:
        break
for i in range(m):
    for j in range(n - 1):
        print(matrix[i][j], end=' ')
    print(matrix[i][n - 1])