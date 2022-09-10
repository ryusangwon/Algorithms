n = int(input())
arr = list(map(int, input().split()))

num = 0
arr.sort(reverse=True)
max_num = arr[0]

for i in range(n):
    if n <= 0:
        break
    n -= arr[i]
    num += 1

print(num)