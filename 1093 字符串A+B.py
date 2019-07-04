"""
给定两个字符串 A 和 B，本题要求你输出 A+B，即两个字符串的并集。要求先输出 A，再输出 B，但重复的字符必须被剔除。

输入格式：

输入在两行中分别给出 A 和 B，均为长度不超过 10
?6
?? 的、由可见 ASCII 字符 (即码值为32~126)和空格组成的、由回车标识结束的非空字符串。

输出格式：

在一行中输出题面要求的 A 和 B 的和。

输入样例：

This is a sample test
to show you_How it works
输出样例：

This ampletowyu_Hrk
"""

#########################################
"""
简单，一次通过
1. 善用python的集合去重
2. 因集合无序，最后有序输出，可用listA.sort(key=listA.index),即可使集合（使用时，需首先把集合转化为list）按照listA的顺序排列
"""
#########################################

A = list(input())
B = list(input())
C = list(set(A).union(set(B)))
C.sort(key=(A+B).index)
print(''.join(C))