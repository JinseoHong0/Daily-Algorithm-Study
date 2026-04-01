def fill(i, j, k):
    for s in range(i, j+1):
        numList[s-1] = k

import sys
N, M = map(int, sys.stdin.readline().split())

numList = [0]*N

for loop in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    fill(i, j, k)
    
print(*(numList))
