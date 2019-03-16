#给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：

#    A​1​​ = 能被 5 整除的数字中所有偶数的和；
#    A​2​​ = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 n​1​​−n​2​​+n​3​​−n​4​​⋯；
#    A​3​​ = 被 5 除后余 2 的数字的个数；
#    A​4​​ = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
#    A​5​​ = 被 5 除后余 4 的数字中最大数字。

#输入格式：

#每个输入包含 1 个测试用例。每个测试用例先给出一个不超过 1000 的正整数 N，随后给出 N 个不超过 1000 的待分类的正整数。数字间以空格分隔。
#输出格式：

#对给定的 N 个正整数，按题目要求计算 A​1​​~A​5​​ 并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。

#若其中某一类数字不存在，则在相应位置输出 N。
#输入样例 1：

#13 1 2 3 4 5 6 7 8 9 10 20 16 18

#输出样例 1：

#30 11 2 9.7 9

#输入样例 2：

#8 1 2 4 5 6 7 9 16

#输出样例 2：

#N 11 2 N 9
num = str(input())
num = num.split()
num = list(map(int,num))
length = len(num)
i = 1
A = ['N'] * 5
temp1 = 0
temp2 = 0
flag = 1
temp3 = 0
temp4 = 0
count = 0
while i < length:
    if num[i] % 10 == 0:
        temp1 += num[i]
        A[0] = temp1
    elif num[i] % 5 == 1:
        temp2 += flag * num[i]
        flag = -flag
        A[1] = temp2
    elif num[i] % 5 == 2:
        temp3 +=1
        A[2] = temp3
    elif num[i] % 5 == 3:
        temp4 += num[i]
        A[3] = temp4
        count += 1
    elif num[i] % 5 == 4:
        if A[4] == 'N':
            A[4] = num[i]
        else:
            if A[4] < num[i]:
                A[4] = num[i]
    i+=1
if A[3] != 'N':
    A[3] = A[3] / count
    A[3] = int(A[3] * 10 + 0.5)
    A[3] = A[3] / 10.0
    A[3] = str(A[3])
A = list(map(str,A))
print(' '.join(A))