'''
字符串 APPAPT 中包含了两个单词 PAT，其中第一个 PAT 是第 2 位(P)，第 4 位(A)，第 6 位(T)；第二个 PAT 是第 3 位(P)，第 4 位(A)，第 6 位(T)。

现给定字符串，问一共可以形成多少个 PAT？
输入格式：

输入只有一行，包含一个字符串，长度不超过10​5​​，只包含 P、A、T 三种字母。
输出格式：

在一行中输出给定字符串中包含多少个 PAT。由于结果可能比较大，只输出对 1000000007 取余数的结果。
输入样例：

APPAPT

输出样例：

2

'''

##################################################################################################
'''
这题目主要是超时问题，这是由不优秀的算法造成的
一开始的想法就是暴力遍历，循环查找，找到P，然后找其后面的A，然后再找其后面的T，不断+1
后面借鉴了网上的思路，某个P能形成多少个PAT，取决于该P后面有多少AT；而某个A能形成多少AT，取决于该A后面有多少T。因此可以逆序逐个统计到相应位置，有多少T，有多少AT，有多少PAT：
    T=T+1;AT=AT+T;PAT=PAT+AT
python 字符串逆序方法：
    string[::-1]
'''
##################################################################################################

'''
#2、3、4超时
line = input()
total = 0
index_p = 0
while True:
    try:
        index_p = line.index('P',index_p) + 1
        index_a = index_p
        while True:
            try:
                index_a = line.index('A',index_a) + 1
                index_t = index_a
                while True:
                    try:
                        index_t = line.index('T',index_t) + 1
                        total += 1
                    except:
                        break
            except:
                break
    except:
        break
print(total % 1000000007)
'''
#############################################
#############################################
'''
#2、3、4超时
line = input()
total = 0
index_p = 0
while True:
    try:
        index_p = line.index('P',index_p) + 1
        index_a = index_p
        while True:
            try:
                index_a = line.index('A',index_a) + 1
                index_t = index_a
                total += line.count('T',index_t)
            except:
                break
    except:
        break
print(total % 1000000007)
'''
################################################
################################################
line = input()
line = line[::-1]
numT, numAT, numPAT = 0, 0, 0
for i in line:
    if i == 'T':
        numT += 1
    elif i == 'A':
        numAT += numT
    elif i == 'P':
        numPAT += numAT
print(numPAT % 1000000007)