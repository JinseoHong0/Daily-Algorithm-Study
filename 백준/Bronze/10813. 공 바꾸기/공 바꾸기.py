import sys
N, M = map(int, sys.stdin.readline().split())
numList = list(range(1, N+1))
for k in range(M):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    numList[i], numList[j] = numList[j], numList[i]

print(*(numList))
