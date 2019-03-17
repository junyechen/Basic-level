#正整数 A 的“D​A​​（为 1 位整数）部分”定义为由 A 中所有 D​A​​ 组成的新整数 P​A​​。例如：给定
#A=3862767，D​A​​=6，则 A 的“6 部分”P​A​​ 是 66，因为 A 中有 2 个 6。

#现给定 A、D​A​​、B、D​B​​，请编写程序计算 P​A​​+P​B​​。
#输入格式：

#输入在一行中依次给出 A、D​A​​、B、D​B​​，中间以空格分隔，其中 0<A,B<10​10​​。
#输出格式：

#在一行中输出 P​A​​+P​B​​ 的值。
#输入样例 1：

#3862767 6 13530293 3

#输出样例 1：

#399

#输入样例 2：

#3862767 1 13530293 8

#输出样例 2：

#0

line = input().split()
A = line[0]
DA = line[1]
B = line[2]
DB = line[3]
locA = 0
PA = 0
while locA < len(A):
    locA = A.find(DA,locA)
    if locA == -1:
        break
    else:
        PA = PA + 1
        locA = locA + 1
if PA == 0:
    PA = 0
else:
    PA = int(DA * PA)
locB = 0
PB = 0
while locB < len(B):
    locB = B.find(DB,locB)
    if locB == -1:
        break
    else:
        PB = PB + 1
        locB = locB + 1
if PB == 0:
    PB = 0
else:
    PB = int(DB * PB)
print(PA + PB)