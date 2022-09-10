n, m = map(int, input().split())
arr = list(map(int, input().split()))

num = n * int((n-1) / 2)
num = int(n * (n-1)/2)
print(num)
for i in range(0, len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            num -= 1

print(num)