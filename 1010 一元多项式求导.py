#设计函数求一元多项式的导数。（注：x​n​​（n为整数）的一阶导数为nx​n−1​​。）
#输入格式:

#以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过 1000 的整数）。数字间以空格分隔。
#输出格式:

#以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格。注意“零多项式”的指数和系数都是 0，但是表示为 0
#0。
#输入样例:

#3 4 -5 2 6 1 -2 0

#输出样例:

#12 3 -10 1 6 0

#
#坑点：
#1、输出非零项系数和指数，因此求导后系数变0的不要输出
#2、零多项式输出 0 0，即求导后为0，应输出0 0
#3、数字间以空格分隔，没有说有多少空格
polynomial = str(input())
polynomial = polynomial.split()
length = len(polynomial)
derivative = []
i = 0
while i < length:
    if polynomial[i + 1] != '0' and polynomial[i] != '0':
            derivative.append(str(int(polynomial[i + 1]) * int(polynomial[i])))
            derivative.append(str(int(polynomial[i + 1]) - 1))
    i += 2
if derivative == []:
    derivative = ['0','0']
print(' '.join(derivative))