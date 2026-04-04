a, b = map(int, input().split())
arr1, arr2 = [],[]


for i in range(a):
    a1 = list(map(int, input().split()))
    arr1.append(a1)
             
for i in range(a):
    b1 = list(map(int, input().split()))
    arr2.append(b1)


for i in range(a):
    for j in range(b):
        result = arr1[i][j] + arr2[i][j]
        print(result,end=' ')
    print()
