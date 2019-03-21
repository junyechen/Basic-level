#给定一个常数 K 以及一个单链表 L，请编写程序将 L 中每 K 个结点反转。例如：给定 L 为 1→2→3→4→5→6，K 为 3，则输出应该为 3→2→1→6→5→4；如果 K 为 4，则输出应该为 4→3→2→1→5→6，即最后不到 K 个元素不反转。
#输入格式：

#每个输入包含 1 个测试用例。每个测试用例第 1 行给出第 1 个结点的地址、结点总个数正整数 N (≤10​5​​)、以及正整数 K (≤N)，即要求反转的子链结点的个数。结点的地址是 5 位非负整数，NULL 地址用 −1 表示。

#接下来有 N 行，每行格式为：

#Address Data Next

#其中 Address 是结点地址，Data 是该结点保存的整数数据，Next 是下一结点的地址。

#1.利用for range可以替代while方法
#2.数据量太大，超时问题python无法解决

line = input().split()
head, nodeTotal, reverseNodeNum = line[0], int(line[1]), int(line[2])
line = []
for i in range(nodeTotal):
    line.append(list(input().split()))
i = 0
linkedList = []
for i in range(nodeTotal):
    if line[i][0] == head:
        linkedList.append(line[i])
        nextNode = line[i][2]
        del line[i]
        break
while linkedList[-1][2] != '-1':
    index = 0
    while line[index][0] != nextNode:
        index += 1
    linkedList.append(line[index])
    nextNode = line[index][2]
    del line[index]
for i in range(0,len(linkedList) - reverseNodeNum + 1,reverseNodeNum):
    TempList = linkedList[i:i + reverseNodeNum]
    TempList.reverse()
    linkedList[i:i + reverseNodeNum] = TempList
for i in range(len(linkedList) - 1):
    linkedList[i][2] = linkedList[i + 1][0]
linkedList[-1][2] = '-1'
linkedList = [' '.join(node) for node in linkedList]
for node in linkedList:
    print(node)