"""
批改多选题是比较麻烦的事情，本题就请你写个程序帮助老师批改多选题，并且指出哪道题错的人最多。
输入格式：

输入在第一行给出两个正整数 N（≤ 1000）和 M（≤ 100），分别是学生人数和多选题的个数。随后 M 行，每行顺次给出一道题的满分值（不超过 5 的正整数）、选项个数（不少于 2 且不超过 5 的正整数）、正确选项个数（不超过选项个数的正整数）、所有正确选项。注意每题的选项从小写英文字母 a 开始顺次排列。各项间以 1 个空格分隔。最后 N 行，每行给出一个学生的答题情况，其每题答案格式为 (选中的选项个数 选项1 ……)，按题目顺序给出。注意：题目保证学生的答题情况是合法的，即不存在选中的选项数超过实际选项数的情况。
输出格式：

按照输入的顺序给出每个学生的得分，每个分数占一行。注意判题时只有选择全部正确才能得到该题的分数。最后一行输出错得最多的题目的错误次数和编号（题目按照输入的顺序从 1 开始编号）。如果有并列，则按编号递增顺序输出。数字间用空格分隔，行首尾不得有多余空格。如果所有题目都没有人错，则在最后一行输出 Too simple。
输入样例：

3 4 
3 4 2 a c
2 5 1 b
5 3 2 b c
1 5 4 a b d e
(2 a c) (2 b d) (2 a c) (3 a b e)
(2 a c) (1 b) (2 a b) (4 a b d e)
(2 b d) (1 e) (2 b c) (4 a b c d)

输出样例：

3
6
5
2 2 3 4
"""

N, M = [int(i) for i in input().split()]
answer = []
score = [0] * N
result = [0] * M
for i in range(M):
    answer.append(input())
for i in range(N):
    answer_ = input().split('(')
    for j in range(M):
        if answer_[j + 1].split(')')[0] != answer[j][4:]:
            result[j] += 1
        else:
            score[i] += int(answer[j][0])
for i in range(N):
    print(score[i])
#temp = list(zip(range(M),result))
#temp = sorted(temp,key=lambda x:x[1],reverse=True)
temp = list(zip(range(M),result))
temp.sort(key=lambda x:x[1],reverse=True)
if temp[0][1] == 0:
    print("Too simple")
else:
    high = temp[0][1]
    print(high,end='')
    for i in range(M):
        if temp[i][1] == high:
            print('',temp[i][0] + 1,end='')