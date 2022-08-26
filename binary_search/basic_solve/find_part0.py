n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

for i in range(m):
    check = 0
    for j in range(n):
        if arr1[j] == arr2[i]:
            check=1

    if check == 0:
        print("no")
    else:
        print("yes")