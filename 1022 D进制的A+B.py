#输入两个非负 10 进制整数 A 和 B (≤2​30​​−1)，输出 A+B 的 D (1<D≤10)进制数。
#输入格式：

#输入在一行中依次给出 3 个整数 A、B 和 D。
#输出格式：

#输出 A+B 的 D 进制数。
#输入样例：

#123 456 8

#输出样例：

#1103

line = input().split()
A = line[0]
B = line[1]
D = int(line[2])
length = min(len(A),len(B))
C = []
digit = 1
carry = 0
while digit <= length or carry == 1:
    try:
        sum = int(A[-digit]) + int(B[-digit]) + carry
    except:
        try:
            sum = int(A[-digit]) + carry
        except:
            try:
                sum = int(B[-digit]) + carry
            except:
                 C.insert(0,'1')
                 break
    if sum > 10:
        C.insert(0,str(sum - 10))
        carry = 1
    else:
        C.insert(0,str(sum))
        carry = 0
    digit += 1
if len(A) > len(B):
    C.insert(0,A[0:len(A) - digit])
elif len(A) < len(B):
    C.insert(0,B[0:len(B) - digit])
C = ''.join(C)
conver = []
while True:
    carry = 0
    quotient = ''
    for i in C:
        dividend = carry * 10 + int(i)
        quotient += str(dividend // D)
        carry = dividend % D
    C = quotient
    conver.append(str(carry))
    if C == '0':
        break
    i = 0
    while C[i] == '0':
        i += 1
    C = C[i:]
print(''.join(conver[::-1]))