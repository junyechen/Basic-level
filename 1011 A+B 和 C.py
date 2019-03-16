
#给定区间 [−2​31​​,2​31​​] 内的 3 个整数 A、B 和 C，请判断 A+B 是否大于 C。
#输入格式：

#输入第 1 行给出正整数 T (≤10)，是测试用例的个数。随后给出 T 组测试用例，每组占一行，顺序给出 A、B 和 C。整数间以空格分隔。
#输出格式：

#对每组测试用例，在一行中输出 Case #X: true 如果 A+B>C，否则输出 Case #X: false，其中 X 是测试用例的编号（从 1 开始）。

T = int(input())
case = []

for i in range(T):
    num = str(input())
    num = num.split()
    if int(num[0]) + int(num[1]) > int(num[2]):
        case.append('true')
    else:
        case.append('false')

for i in range(T):
    print("Case #" + str(i + 1) + ": " + case[i])