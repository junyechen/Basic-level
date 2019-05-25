"""
拍集体照时队形很重要，这里对给定的 N 个人 K 排的队形设计排队规则如下：

    每排人数为 N/K（向下取整），多出来的人全部站在最后一排；

    后排所有人的个子都不比前排任何人矮；

    每排中最高者站中间（中间位置为 m/2+1，其中 m 为该排人数，除法向下取整）；

    每排其他人以中间人为轴，按身高非增序，先右后左交替入队站在中间人的两侧（例如5人身高为190、188、186、175、170，则队形为175、188、190、186、170。这里假设你面对拍照者，所以你的左边是中间人的右边）；

    若多人身高相同，则按名字的字典序升序排列。这里保证无重名。

现给定一组拍照人，请编写程序输出他们的队形。
输入格式：

每个输入包含 1 个测试用例。每个测试用例第 1 行给出两个正整数 N（≤10​4​​，总人数）和 K（≤10，总排数）。随后 N 行，每行给出一个人的名字（不包含空格、长度不超过 8 个英文字母）和身高（[30, 300] 区间内的整数）。
输出格式：

输出拍照的队形。即K排人名，其间以空格分隔，行末不得有多余空格。注意：假设你面对拍照者，后排的人输出在上方，前排输出在下方。
输入样例：

10 3
Tom 188
Mike 170
Eva 168
Tim 160
Joe 190
Ann 168
Bob 175
Nick 186
Amy 160
John 159

输出样例：

Bob Tom Joe Nick
Ann Mike Eva
Tim Amy John
"""

##################################################################
"""
1. 本题可在初始桶排序后，直接得出由高到低的顺序列表；
2. 在排队时，不用按照一左一右顺序，而可以先完成左边，再完成右边，只要插入数据间隔2就可以做到
3. 注意只有1排时的特殊情况
"""
##################################################################

N, K = [int(i) for i in input().split()]
height = [0] * 301
max = 30
min = 300
for i in range(N):
    name, height_ = input().split()
    height_ = int(height_)
    flag = True
    if height_ > max:
        max = height_
    if height_ < min:
        min = height_
    if height[height_] == 0:
        height[height_] = [name]
    else:
        for j in range(len(height[height_])):
            if name < height[height_][j]:
                height[height_].insert(j,name)
                flag = False
                break
        if flag:
            height[height_].append(name)
seq = []
for i in range(max,min - 1,-1):
    if height[i] != 0:
        for j in height[i]:
            seq.append(j)
        if len(seq) == N:
            break
m = N // K
m_ = N - (K - 1) * m
if K != 1:
    sequ = [[0 for i in range(m)] for j in range(K - 1)]
    sequ.insert(0,[0] * m_)
else:
    sequ = [[0] * m]
count = 0
middle = m_ // 2 + 1
left = right = 1
init = 0
sequ[0][middle - 1] = seq[init]
count += 1
while left < middle:
    sequ[0][middle - 1 - left] = seq[init + left * 2 - 1]
    left += 1
    count += 1
while right < m_ - middle + 1:
    sequ[0][middle - 1 + right] = seq[init + right * 2]
    right += 1
    count += 1
row = 1
middle = m // 2 + 1
while row < K:
    left = right = 1
    init = m_ + m * (row - 1)
    sequ[row][middle - 1] = seq[init]
    count += 1
    while left < middle:
        sequ[row][middle - 1 - left] = seq[init + left * 2 - 1]
        left += 1
        count += 1
    while right < m - middle + 1:
        sequ[row][middle - 1 + right] = seq[init + right * 2]
        right += 1
        count += 1
    row += 1
if K != 1:
    for i in range(K):
        for j in sequ[i][:-1]:
            print(j,end=' ')
        print(sequ[i][-1])
else:
    for j in sequ[0][:-1]:
        print(j,end=' ')
    print(sequ[0][-1])




"""
N, K = [int(i) for i in input().split()]
height = [0] * 301
max = 30
min = 300
for i in range(N):
    name, height_ = input().split()
    height_ = int(height_)
    flag = True
    if height_ > max:
        max = height_
    if height_ < min:
        min = height_
    if height[height_] == 0:
        height[height_] = [name]
    else:
        for j in range(len(height[height_])):
            if name < height[height_][j]:
                height[height_].insert(j,name)
                flag = False
                break
        if flag:
            height[height_].append(name)
m = N // K
m_ = N - (K - 1) * m
if K != 1:
    sequ = [[0 for i in range(m)] for j in range(K - 1)]
    sequ.insert(0,[0] * m_)
else:
    sequ = [0] * m
row = 1
middle_ = m_ // 2 + 1
middle = m // 2 + 1
right = middle_
left = middle_ - 1
flag = True
count = 0
try:
    for i in range(max,min - 1,-1):
        if height[i] != 0:
            for j in height[i]:
                if flag:
                    column = right
                else:
                    column = left
                sequ[row - 1][column - 1] = j
                if flag:
                    right += 1
                    flag = not flag
                else:
                    left -= 1
                    flag = not flag
                if left < 1 and right > m_:
                    right = m // 2 + 1
                    left = right - 1
                    m_ = m
                    row += 1
                count+=1
                if count == N:
                    raise Exception
except:
    for i in range(K):
        for j in sequ[i][:-1]:
            print(j,end=' ')
        print(sequ[i][-1])
"""