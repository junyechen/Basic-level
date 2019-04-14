'''
旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。现在给出应该输入的一段文字、以及坏掉的那些键，打出的结果文字会是怎样？
输入格式：

输入在 2 行中分别给出坏掉的那些键、以及应该输入的文字。其中对应英文字母的坏键以大写给出；每段文字是不超过 10​5​​ 个字符的串。可用的字符包括字母 [a-z, A-Z]、数字 0-9、以及下划线 _（代表空格）、,、.、-、+（代表上档键）。题目保证第 2 行输入的文字串非空。

注意：如果上档键坏掉了，那么大写的英文字母无法被打出。
输出格式：

在一行中输出能够被打出的结果文字。如果没有一个字符能被打出，则输出空行。
输入样例：

7+IE.
7_This_is_a_test.

输出样例：

_hs_s_a_tst
'''

#########################################################
'''
这题非常简单，一次通过
更新了一下新的方法，使代码更简洁：
1.  str.upper()可以自动判断是否是英文字母，并将其转换成为大写字母，
    所以不需要像方法一那样繁琐的判断
2.  此外，将算法逻辑调整：
    不需要提前判断shift档
    而是，直接将所有输入字符大写化进行判断：
        若存在坏键列表中，则pass；
        若不存在坏键列表中，则只需判断是否是因大小写字母引起的不存在：
            若shift档没有坏，表明大写可以输出，该字符可以输出
            若shift档损坏，则只要该字符不是大写字母，也可输出
'''
#########################################################
'''
#broken = input()
#input_ = input()
#output_ = []
#if '+' in broken:
#    for i in input_:
#        if i.isalpha():
#            if i.isupper():
#                continue
#            else:
#                if i.upper() in broken:
#                    continue
#                else:
#                    output_.append(i)
#        else:
#            if i in broken:
#                continue
#            else:
#                output_.append(i)
#else:
#    for i in input_:
#        if i.isalpha():
#            if i.upper() in broken:
#                continue
#            else:
#                output_.append(i)
#        else:
#            if i in broken:
#                continue
#            else:
#                output_.append(i)
#if output_:
#    print(''.join(output_))
#else:
#    print('')
'''
#######################################################
#方法2
broken = input()
input_ = input()
output_ = ''
broken_shift = '+' in broken
for i in input_:
    if i.upper() not in broken:
        if not broken_shift or not i.isupper():
            output_ += i
print(output_)
########################################################