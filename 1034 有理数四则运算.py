'''
本题要求编写程序，计算 2 个有理数的和、差、积、商。
输入格式：

输入在一行中按照 a1/b1 a2/b2 的格式给出两个分数形式的有理数，其中分子和分母全是整型范围内的整数，负号只可能出现在分子前，分母不为 0。
输出格式：

分别在 4 行中按照 有理数1 运算符 有理数2 = 结果 的格式顺序输出 2 个有理数的和、差、积、商。注意输出的每个有理数必须是该有理数的最简形式 k a/b，其中 k 是整数部分，a/b 是最简分数部分；若为负数，则须加括号；若除法分母为 0，则输出 Inf。题目保证正确的输出中没有超过整型范围的整数。
输入样例 1：

2/3 -4/2

输出样例 1：

2/3 + (-2) = (-1 1/3)
2/3 - (-2) = 2 2/3
2/3 * (-2) = (-1 1/3)
2/3 / (-2) = (-1/3)

输入样例 2：

5/3 0/6

输出样例 2：

1 2/3 + 0 = 1 2/3
1 2/3 - 0 = 1 2/3
1 2/3 * 0 = 0
1 2/3 / 0 = Inf
'''

##############################################################
'''
1次通过
最简式，因此需要求出最大公约数，采用辗转相除法获得最大公约数
'''
##############################################################

def hcm(a,b):
    if a % b == 0:
        return b
    else:
        return hcm(b,a % b)

def trans(a, b):
    if b == 0:
        return('Inf')
    if a * b < 0:
        flag = True
    else:
        flag = False
    a = abs(a)
    b = abs(b)
    hcm_ = hcm(a,b)
    a = a // hcm_
    b = b // hcm_
    if a % b == 0:
        if flag:
            return '(-' + str(a // b) + ')'
        else:
            return str(a // b)
    else:
        k = a // b
        a = a % b
        if k == 0:
            if flag:
                return '(-' + str(a) + '/' + str(b) + ')'
            else:
                return str(a) + '/' + str(b)
        else:
            if flag:
                return '(-' + str(k) + ' ' + str(a) + '/' + str(b) + ')'
            else:
                return str(k) + ' ' + str(a) + '/' + str(b)

a, b = input().split()
a1, b1 = [int(i) for i in a.split('/')]
a2, b2 = [int(i) for i in b.split('/')]
a = trans(a1, b1)
b = trans(a2, b2)
print(a,'+',b,'=',trans(a1 * b2 + a2 * b1,b1 * b2))
print(a,'-',b,'=',trans(a1 * b2 - a2 * b1,b1 * b2))
print(a,'*',b,'=',trans(a1 * a2,b1 * b2))
print(a,'/',b,'=',trans(a1 * b2,a2 * b1))