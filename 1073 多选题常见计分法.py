"""
批改多选题是比较麻烦的事情，有很多不同的计分方法。有一种最常见的计分方法是：如果考生选择了部分正确选项，并且没有选择任何错误选项，则得到 50% 分数；如果考生选择了任何一个错误的选项，则不能得分。本题就请你写个程序帮助老师批改多选题，并且指出哪道题的哪个选项错的人最多。
输入格式：

输入在第一行给出两个正整数 N（≤1000）和 M（≤100），分别是学生人数和多选题的个数。随后 M 行，每行顺次给出一道题的满分值（不超过 5 的正整数）、选项个数（不少于 2 且不超过 5 的正整数）、正确选项个数（不超过选项个数的正整数）、所有正确选项。注意每题的选项从小写英文字母 a 开始顺次排列。各项间以 1 个空格分隔。最后 N 行，每行给出一个学生的答题情况，其每题答案格式为 (选中的选项个数 选项1 ……)，按题目顺序给出。注意：题目保证学生的答题情况是合法的，即不存在选中的选项数超过实际选项数的情况。
输出格式：

按照输入的顺序给出每个学生的得分，每个分数占一行，输出小数点后 1 位。最后输出错得最多的题目选项的信息，格式为：错误次数 题目编号（题目按照输入的顺序从1开始编号）-选项号。如果有并列，则每行一个选项，按题目编号递增顺序输出；再并列则按选项号递增顺序输出。行首尾不得有多余空格。如果所有题目都没有人错，则在最后一行输出 Too simple。
输入样例 1：

3 4 
3 4 2 a c
2 5 1 b
5 3 2 b c
1 5 4 a b d e
(2 a c) (3 b d e) (2 a c) (3 a b e)
(2 a c) (1 b) (2 a b) (4 a b d e)
(2 b d) (1 e) (1 c) (4 a b c d)

输出样例 1：

3.5
6.0
2.5
2 2-e
2 3-a
2 3-b

输入样例 2：

2 2 
3 4 2 a c
2 5 1 b
(2 a c) (1 b)
(2 a c) (1 b)

输出样例 2：

5.0
5.0
Too simple
"""

###############################################################
"""
在检测错误答案时，使用列表，并标记最大值，在最后输出时，遍历列表值，找到最大值，从而输出题号；
不需要使用字典等方法，因为排序更花费时间，多于从头到尾遍历一次的时间
"""
###############################################################

N, M = [int(i) for i in input().split()]
answer = []
wrong_ans = []
max_wrong = 0
for i in range(M):
    answer.append(input().split())
    for j in range(3):
        answer[i][j] = int(answer[i][j])
    wrong_ans.append([0] * answer[i][1])
for i in range(N):
    result = input().split('(')
    grade = 0
    for j in range(1,len(result)):
        result[j] = result[j].split(')')[0].split()
        choice = int(result[j][0])
        right, wrong = 0, 0
        right_ans = answer[j - 1][3:]
        for k in result[j][1:]:
            if k in answer[j - 1][3:]:
                right += 1
                right_ans.remove(k)
            else:
                wrong += 1
                wrong_ans[j - 1][ord(k) - 97] += 1
                if wrong_ans[j - 1][ord(k) - 97] > max_wrong:
                    max_wrong = wrong_ans[j - 1][ord(k) - 97]
        for k in right_ans:
            wrong_ans[j - 1][ord(k) - 97] += 1
            if wrong_ans[j - 1][ord(k) - 97] > max_wrong:
                    max_wrong = wrong_ans[j - 1][ord(k) - 97]
        if right == 0:
            pass
        elif right == answer[j - 1][2] and wrong == 0:
            grade += answer[j - 1][0]
        elif wrong == 0:
            grade += answer[j - 1][0] / 2
        elif wrong != 0:
            pass
    print("%.1f" % grade)
if max_wrong == 0:
    print("Too simple")
else:
    for i in range(M):
        for j in range(len(wrong_ans[i])):
            if wrong_ans[i][j] == max_wrong:
                print(max_wrong,str(i + 1) + '-' + chr(j + 97))
        
"""
N, M = [int(i) for i in input().split()]
answer = []
wrong_ans = dict()
for i in range(M):
    answer.append(input().split())
    for j in range(3):
        answer[i][j] = int(answer[i][j])
    for j in range(answer[i][1]):
        wrong_ans[(str(i + 1)) + '-' + chr(97 + j)] = 0
for i in range(N):
    result = input().split('(')
    grade = 0
    for j in range(1,len(result)):
        result[j] = result[j].split(')')[0].split()
        choice = int(result[j][0])
        right, wrong = 0, 0
        right_ans = answer[j - 1][3:]
        for k in result[j][1:]:
            if k in answer[j - 1][3:]:
                right += 1
                right_ans.remove(k)
            else:
                wrong += 1
                wrong_ans[str(j) + '-' + k] += 1
        for k in right_ans:
            wrong_ans[str(j) + '-' + k] += 1
        if right == 0:
            pass
        elif right == answer[j - 1][2] and wrong == 0:
            grade += answer[j - 1][0]
        elif wrong == 0:
            grade += answer[j - 1][0] / 2
        elif wrong != 0:
            pass
    print("%.1f" % grade)
wrong_ans = sorted(wrong_ans.items(),key=lambda x:x[1],reverse=True)
if wrong_ans[0][1] == 0:
    print("Too simple")
else:
    max_wrong = wrong_ans[0][1]
    print(max_wrong,wrong_ans[0][0])
    i = 1
    while True:
        if wrong_ans[i][1] == max_wrong:
            print(max_wrong,wrong_ans[i][0])
        else:
            break
        i += 1
"""