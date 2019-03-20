#科学计数法是科学家用来表示很大或很小的数字的一种方便的方法，其满足正则表达式 [+-][1-9].[0-9]+E[+-][0-9]+，即数字的整数部分只有 1 位，小数部分至少有 1 位，该数字及其指数部分的正负号即使对正数也必定明确给出。

#现以科学计数法的格式给出实数 A，请编写程序按普通数字表示法输出 A，并保证所有有效位都被保留。
#输入格式：

#每个输入包含 1 个测试用例，即一个以科学计数法表示的实数 A。该数字的存储长度不超过 9999 字节，且其指数的绝对值不超过 9999。
#输出格式：

#对每个测试用例，在一行中按普通数字表示法输出 A，并保证所有有效位都被保留，包括末尾的 0。
#输入样例 1：

#+1.23400E-03

#输出样例 1：

#0.00123400

#输入样例 2：

#-1.2E+10

#输出样例 2：

#-12000000000

#注意输出要求，正数无需输出'+'号
A = input()
Eloc = A.find('E')
exponent = int(A[Eloc + 1:])
effective_digit = A[0:2] + A[3:Eloc]
if exponent > 0:
    if len(effective_digit) - 2 > exponent:
        result = effective_digit[0:2 + exponent] + '.' + effective_digit[2 + exponent:]
    elif len(effective_digit) - 2 == exponent:
        result = effective_digit
    else:
        result = effective_digit + '0' * (exponent - (len(effective_digit) - 2))
elif exponent == 0:
    if len(effective_digit)-1==2 and effective_digit[-1]=='0':
        result=effective_digit[0:2]
    else:
        result = A[0:Eloc]
else:
    result = effective_digit[0] + '0.' + '0' * (abs(exponent) - 1) + effective_digit[1:]
if result[0] == '+':
    result = result[1:]
print(result)