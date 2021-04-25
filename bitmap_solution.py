import math
from collections import deque



def distance(a:int,b:int,c:int,d:int)->int:
    return int(math.fabs(a-c) + math.fabs(b-d))
 
def in_range(a,b, n, m):
    return (a >= 0 and a < n) and (b >= 0 and b < m)
 
def dynamic_solution(matrix,n,m):
    maximum = n*m;
    dp = [[0 if matrix[j][i] == 1 else maximum for i in range(m)] for j in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    for i in range(n):
        for j in range(m):
            minimum = maximum
            for d1,d2 in directions:
                x,y = i + d1, j +d2
                if in_range(x,y,n,m) and not matrix[i][j] == 1:
                    minimum = min(minimum,dp[x][y])
            if not minimum == maximum: dp[i][j] = minimum +1

    for i in range(n):
        k = (n-1) - i
        for j in range(m):
            l = (m-1) - j
            minimum = maximum
            for d1, d2 in directions:
                x,y = k + d1, l + d2
                if in_range(x,y,n,m) and not matrix[k][l] == 1:
                    minimum = min(minimum,dp[x][y])
            if not minimum == maximum:
                dp[k][l] = minimum + 1

    return dp


cases = []
iters = int(input())
for i in range(iters):
    dimensions = input().split()
    n,m = int(dimensions[0]),int(dimensions[1])
    
    matrix = [[int(x) for x in input()] for k in range(n)]
    cases.append(matrix)
    input()
 
 
 
for case in cases:
    result = dynamic_solution(case,len(case),len(case[0]))
    for l in result:
        s = str(l[0])
        for i in range(1,len(l)):
            s = s +' ' + str(l[i]) 
        print(s)
     