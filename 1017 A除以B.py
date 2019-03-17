#本题要求计算 A/B，其中 A 是不超过 1000 位的正整数，B 是 1 位正整数。你需要输出商数 Q 和余数 R，使得 A=B×Q+R 成立。
#输入格式：

#输入在一行中依次给出 A 和 B，中间以 1 空格分隔。
#输出格式：

#在一行中依次输出 Q 和 R，中间以 1 空格分隔。
#输入样例：

#123456789050987654321 7

#输出样例：

#17636684150141093474 3

line = input().split()
A = line[0]
B = int(line[1])
Q = ''
while len(A) > 2:
    A_ = int(A[0])
    if A_ // B > 0:
        Q = Q + str(A_ // B)
        A = str(A_ % B) + A[1:]
    else:
        A_ = int(A[0:2])
        Q = Q + str(A_ // B)
        A = str(A_ % B) + A[2:]
A_ = int(A)
Q = Q + str(A_ // B)
R = str(A_ % B)
print(Q,R)