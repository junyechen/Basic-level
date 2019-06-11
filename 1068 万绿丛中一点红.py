"""
对于计算机而言，颜色不过是像素点对应的一个 24 位的数值。现给定一幅分辨率为 M×N 的画，要求你找出万绿丛中的一点红，即有独一无二颜色的那个像素点，并且该点的颜色与其周围 8 个相邻像素的颜色差充分大。
输入格式：

输入第一行给出三个正整数，分别是 M 和 N（≤ 1000），即图像的分辨率；以及 TOL，是所求像素点与相邻点的颜色差阈值，色差超过 TOL 的点才被考虑。随后 N 行，每行给出 M 个像素的颜色值，范围在 [0,2​24​​) 内。所有同行数字间用空格或 TAB 分开。
输出格式：

在一行中按照 (x, y): color 的格式输出所求像素点的位置以及颜色值，其中位置 x 和 y 分别是该像素在图像矩阵中的列、行编号（从 1 开始编号）。如果这样的点不唯一，则输出 Not Unique；如果这样的点不存在，则输出 Not Exist。
输入样例 1：

8 6 200
0 	 0 	  0 	   0	    0 	     0 	      0        0
65280 	 65280    65280    16711479 65280    65280    65280    65280
16711479 65280    65280    65280    16711680 65280    65280    65280
65280 	 65280    65280    65280    65280    65280    165280   165280
65280 	 65280 	  16777015 65280    65280    165280   65480    165280
16777215 16777215 16777215 16777215 16777215 16777215 16777215 16777215

输出样例 1：

(5, 3): 16711680

输入样例 2：

4 5 2
0 0 0 0
0 0 3 0
0 0 0 0
0 5 0 0
0 0 0 0

输出样例 2：

Not Unique
    j-1 j   j+1
i-1
i
i+1
        
输入样例 3：

3 3 5
1 2 3
3 4 5
5 6 7

输出样例 3：

Not Exist
"""

############################################################
"""
边界问题，可通过在周边加“一圈”解决
测试点4超时，python无法解决；
用C语言，其他测试点均为2ms，但测试点4需要235ms，是基础运行的100余倍时间
"""
############################################################

M, N, TOL = [int(i) for i in input().split()]
square = [[0 for i in range(M + 2)] for j in range(N + 2)]
for i in range(N):
    square[i + 1][1:-1] = [int(j) for j in input().split()]
candi = []
abadon = []
storage = dict()
for i in range(1,N + 1):
    for j in range(1,M + 1):
        if square[i][j] in abadon:
            continue
        elif square[i][j] in candi:
            candi.remove(square[i][j])
            abadon.append(square[i][j])
        elif abs(square[i][j] - square[i - 1][j]) > TOL and abs(square[i][j] - square[i - 1][j + 1]) > TOL and abs(square[i][j] - square[i][j + 1]) > TOL and abs(square[i][j] - square[i + 1][j + 1]) > TOL and abs(square[i][j] - square[i + 1][j]) > TOL and abs(square[i][j] - square[i + 1][j - 1]) > TOL and abs(square[i][j] - square[i][j - 1]) > TOL and abs(square[i][j] - square[i - 1][j - 1]) > TOL:
            candi.append(square[i][j])
            storage[square[i][j]] = (i,j)
        else:
            abadon.append(square[i][j])
if len(candi) == 0:
    print("Not Exist")
elif len(candi) != 1:
    print("Not Unique")
else:
    print("(%d, %d): %d" % (storage[candi[0]][1],storage[candi[0]][0],candi[0]))
