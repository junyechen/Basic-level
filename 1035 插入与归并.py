'''
根据维基百科的定义：

插入排序是迭代算法，逐一获得输入数据，逐步产生有序的输出序列。每步迭代中，算法从输入序列中取出一元素，将之插入有序序列中正确的位置。如此迭代直到全部元素有序。

归并排序进行如下迭代操作：首先将原始序列看成 N 个只包含 1 个元素的有序子序列，然后每次迭代归并两个相邻的有序子序列，直到最后只剩下 1 个有序的序列。

现给定原始序列和由某排序算法产生的中间序列，请你判断该算法究竟是哪种排序算法？
输入格式：

输入在第一行给出正整数 N (≤100)；随后一行给出原始序列的 N 个整数；最后一行给出由某排序算法产生的中间序列。这里假设排序的目标序列是升序。数字间以空格分隔。
输出格式：

首先在第 1 行中输出Insertion Sort表示插入排序、或Merge Sort表示归并排序；然后在第 2 行中输出用该排序算法再迭代一轮的结果序列。题目保证每组测试的结果是唯一的。数字间以空格分隔，且行首尾不得有多余空格。
输入样例 1：

10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

输出样例 1：

Insertion Sort
1 2 3 5 7 8 9 4 6 0
'''

def Insertion(seq1,seq2):
    flag = False
    for i in range(1,len(seq1)):
        if flag:
            key = seq1[i]
            for j in range(i):
                if key < seq1[j]:
                    seq1.pop(i)
                    seq1.insert(j, key)
                    break
            print('Insertion Sort')
            print(' '.join(map(str,seq1)))
            return flag
        else:
            key = seq1[i]
            for j in range(i):
                if key < seq1[j]:
                    seq1.pop(i)
                    seq1.insert(j,key)
                    break
            if seq1 == seq2:
                flag = True
    return flag

def MergeSort(seq1, seq2):
    i = 1
    flag = False
    while True:
        if flag:
            for j in range(0,len(seq1),i*2):
                l, r = j, j+i
                temp = []
                while l<j+i and r<min(len(seq1),j+i*2):
                    if seq1[l]<seq1[r]:
                        temp.append(seq1[l])
                        l += 1
                    else:
                        temp.append(seq1[r])
                        r += 1
                for p in range(l,j+i):
                    temp.append(seq1[p])
                for p in range(r,min(len(seq1),j+i*2)):
                    temp.append(seq1[p])
                seq1[j:j+i*2]=temp
            print('Merge Sort')
            print(' '.join(map(str,seq1))) 
            return 0
        else:
            for j in range(0,len(seq1),i*2):
                l, r = j, j+i
                temp = []
                while l<j+i and r<min(len(seq1),j+i*2):
                    if seq1[l]<seq1[r]:
                        temp.append(seq1[l])
                        l += 1
                    else:
                        temp.append(seq1[r])
                        r += 1
                for p in range(l,j+i):
                    temp.append(seq1[p])
                for p in range(r,min(len(seq1),j+i*2)):
                    temp.append(seq1[p])
                seq1[j:j+i*2]=temp
                if seq1 == seq2:
                    flag = True
            i = i*2
            if i > len(seq1):
                break
    l, r = 0, i
    temp = []
    while l<j and r<len(seq1):
        if seq1[l]<seq1[r]:
            temp.append(seq1[l])
            l += 1
        else:
            temp.append(seq1[r])
            r += 1
    for p in range(l,j):
        temp.append(seq1[p])
    for p in range(r,seq1):
        temp.append(seq1[p])
    print('Merge Sort')
    print(' '.join(map(str,seq1)))

N = int(input())
seq1 = [int(i) for i in input().split()]
seq2 = [int(i) for i in input().split()]
seq3 = [i for i in seq1]

if not Insertion(seq1, seq2):
    MergeSort(seq3, seq2)


'''
def Isort(n,m):
    x = 0
    for i in range(1,len(n)):
       k = n[:i+1]
       k.sort()
       k.extend(n[i+1:])
       if x==1:
           return k
       if k==m:
           x = 1
    return False
 
def Msort(n,m):
    x = 0
    n = [[i] for i in n]
    while len(n)>1:
        k = []
        for j in range(0,len(n),2):
            try:
                n[j].extend(n[j+1])
                k.append(n[j])
            except:
                k.append(n[j])
        for i in k:
            i = i.sort()
        n = k[:]
        result = []
        for i in k:
            for l in i:
                result.append(l)
        if x==1:
            return result
        if result==m:
            x = 1
    
n = input()
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a1 = a[:]
m = Isort(a,b)
if m!=False:
    print("Insertion Sort")
    for i in range(len(m)-1):
        print(m[i],end=" ")
    print(m[i+1],end="")
else:
    m = Msort(a1,b)
    print("Merge Sort")
    for i in range(len(m)-1):
        print(m[i],end=" ")
    print(m[i+1],end="")
'''