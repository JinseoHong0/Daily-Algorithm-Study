def swap(numList, i, j):
    x = numList[i]
    numList[i] = numList[j]
    numList[j] = x
    

N, M = map(int, input().split())
numList = list(range(1, N+1))

for k in range(M):
    i, j = map(int, input().split())
    while(j>i):
        swap(numList, i-1, j-1)
        i += 1
        j -= 1
numstr = ""
for s in numList:
    numstr += str(s)+" "

print(numstr.rstrip(" "))