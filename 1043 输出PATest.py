'''
给定一个长度不超过 10​4​​ 的、仅由英文字母构成的字符串。请将字符重新调整顺序，按 PATestPATest.... 这样的顺序输出，并忽略其它字符。当然，六种字符的个数不一定是一样多的，若某种字符已经输出完，则余下的字符仍按 PATest 的顺序打印，直到所有字符都被输出。
输入格式：

输入在一行中给出一个长度不超过 10​4​​ 的、仅由英文字母构成的非空字符串。
输出格式：

在一行中按题目要求输出排序后的字符串。题目保证输出非空。
输入样例：

redlesPayBestPATTopTeePHPereatitAPPT

输出样例：

PATestPATestPTetPTePePee

'''
###########################################
'''
非常简单，一次通过
'''
###########################################
store = {'P':0,
         'A':0,
         'T':0,
         'e':0,
         's':0,
         't':0}
for i in input():
    try:
        store[i] += 1
    except:
        pass
sum = 0
for key,value in store.items():
    sum += value
while sum > 0:
    if store['P'] != 0:
        print('P',end='')
        store['P'] -= 1
        sum -= 1
    if store['A'] != 0:
        print('A',end='')
        store['A'] -= 1
        sum -= 1
    if store['T'] != 0:
        print('T',end='')
        store['T'] -= 1
        sum -= 1
    if store['e'] != 0:
        print('e',end='')
        store['e'] -= 1
        sum -= 1
    if store['s'] != 0:
        print('s',end='')
        store['s'] -= 1
        sum -= 1
    if store['t'] != 0:
        print('t',end='')
        store['t'] -= 1
        sum -= 1