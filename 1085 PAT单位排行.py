"""
每次 PAT 考试结束后，考试中心都会发布一个考生单位排行榜。本题就请你实现这个功能。
输入格式：

输入第一行给出一个正整数 N（≤10​5​​），即考生人数。随后 N 行，每行按下列格式给出一个考生的信息：

准考证号 得分 学校

其中准考证号是由 6 个字符组成的字符串，其首字母表示考试的级别：B代表乙级，A代表甲级，T代表顶级；得分是 [0, 100] 区间内的整数；学校是由不超过 6 个英文字母组成的单位码（大小写无关）。注意：题目保证每个考生的准考证号是不同的。
输出格式：

首先在一行中输出单位个数。随后按以下格式非降序输出单位的排行榜：

排名 学校 加权总分 考生人数

其中排名是该单位的排名（从 1 开始）；学校是全部按小写字母输出的单位码；加权总分定义为乙级总分/1.5 + 甲级总分 + 顶级总分*1.5的整数部分；考生人数是该属于单位的考生的总人数。

学校首先按加权总分排行。如有并列，则应对应相同的排名，并按考生人数升序输出。如果仍然并列，则按单位码的字典序输出。
输入样例：

10
A57908 85 Au
B57908 54 LanX
A37487 60 au
T28374 67 CMU
T32486 24 hypu
A66734 92 cmu
B76378 71 AU
A47780 45 lanx
A72809 100 pku
A03274 45 hypu

输出样例：

5
1 cmu 192 2
1 au 192 3
3 pku 100 1
4 hypu 81 2
4 lanx 81 2
"""

############################################################################################
"""
超时问题，再次运行竟然又没有超时，python运行时间比较随意啊！
后来再运行几次，基本是最后2个测试点超时，有几次只有最后1个测试点超时，再没出现再次运行没超时的
需要用C/C++来解决程序运行效率问题
"""
############################################################################################

grades = dict()
for i in range(int(input())):
    temp = input().split()
    school = temp[2].lower()
    if temp[0][0] == 'A':
        weight = 1
    elif temp[0][0] == 'B':
        weight = 1 / 1.5
    elif temp[0][0] == 'T':
        weight = 1.5
    #if school in grades:
    #    grades[school] = [grades[school][0] + weight * int(temp[1]),grades[school][1] + 1]
    #else:
    #    grades[school] = [weight * int(temp[1]),1]
    try:
        grades[school] = [grades[school][0] + weight * int(temp[1]),grades[school][1] + 1]
    except:
        grades[school] = [weight * int(temp[1]),1]
for key,value in grades.items():
    grades[key][0]=int(value[0])
grades = sorted(grades.items(),key=lambda x:(-x[1][0],x[1][1],x[0]))
print(len(grades))
rank, increase, latest = 1, 0, 0
for i in grades:
    if latest == i[1][0]:
        print(rank,i[0],i[1][0],i[1][1])
        increase += 1
    else:
        rank += increase
        increase = 1
        latest = i[1][0]
        print(rank,i[0],i[1][0],i[1][1])