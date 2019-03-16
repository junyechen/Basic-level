#宋代史学家司马光在《资治通鉴》中有一段著名的“德才论”：“是故才德全尽谓之圣人，才德兼亡谓之愚人，德胜才谓之君子，才胜德谓之小人。凡取人之术，苟不得圣人，君子而与之，与其得小人，不若得愚人。”

#现给出一批考生的德才分数，请根据司马光的理论给出录取排名。
#输入格式：

#输入第一行给出 3 个正整数，分别为：N（≤10​5​​），即考生总数；L（≥60），为录取最低分数线，即德分和才分均不低于 L 的考生才有资格被考虑录取；H（<100），为优先录取线——德分和才分均不低于此线的被定义为“才德全尽”，此类考生按德才总分从高到低排序；才分不到但德分到线的一类考生属于“德胜才”，也按总分排序，但排在第一类考生之后；德才分均低于 H，但是德分不低于才分的考生属于“才德兼亡”但尚有“德胜才”者，按总分排序，但排在第二类考生之后；其他达到最低线 L 的考生也按总分排序，但排在第三类考生之后。

#随后 N 行，每行给出一位考生的信息，包括：准考证号 德分 才分，其中准考证号为 8 位整数，德才分为区间 [0, 100] 内的整数。数字间以空格分隔。
#输出格式：

#输出第一行首先给出达到最低分数线的考生人数 M，随后 M 行，每行按照输入格式输出一位考生的信息，考生按输入中说明的规则从高到低排序。当某类考生中有多人总分相同时，按其德分降序排列；若德分也并列，则按准考证号的升序输出。
#输入样例：

#14 60 80
#10000001 64 90
#10000002 90 60
#10000011 85 80
#10000003 85 80
#10000004 80 85
#10000005 82 77
#10000006 83 76
#10000007 90 78
#10000008 75 79
#10000009 59 90
#10000010 88 45
#10000012 80 100
#10000013 90 99
#10000014 66 60

#输出样例：

#12
#10000013 90 99
#10000012 80 100
#10000003 85 80
#10000011 85 80
#10000004 80 85
#10000007 90 78
#10000006 83 76
#10000005 82 77
#10000002 90 60
#10000014 66 60
#10000008 75 79
#10000001 64 90

#########
#python性能问题，用python将有3个测试点超时

line = input().split()
N = int(line[0])
L = int(line[1])
H = int(line[2])
line1 = []
line2 = []
line3 = []
line4 = []
for i in range(N):
    line = str(input())
    line = line.split()
    line = list(map(int,line))
    score = line[1] + line[2]
    line.append(score)
    if line[1] < L or line[2] < L:
        continue
    elif line[1] >= H and line[2] >= H:
        line1.append(line)
    elif line[1] >= H and line[2] < H:
        line2.append(line)
    elif line[1] < H and line[2] < H and line[1] >= line[2]:
        line3.append(line)
    else:
        line4.append(line)
line1.sort(key=(lambda x:[x[3],x[1],-x[0]]),reverse=True)
line2.sort(key=(lambda x:[x[3],x[1],-x[0]]),reverse=True)
line3.sort(key=(lambda x:[x[3],x[1],-x[0]]),reverse=True)
line4.sort(key=(lambda x:[x[3],x[1],-x[0]]),reverse=True)
print(len(line1) + len(line2) + len(line3) + len(line4))
for i in range(len(line1)):
    line1[i] = list(map(str,line1[i]))
    print(' '.join(line1[i][:3]))
for i in range(len(line2)):
    line2[i] = list(map(str,line2[i]))
    print(' '.join(line2[i][:3]))
for i in range(len(line3)):
    line3[i] = list(map(str,line3[i]))
    print(' '.join(line3[i][:3]))
for i in range(len(line4)):
    line4[i] = list(map(str,line4[i]))
    print(' '.join(line4[i][:3]))