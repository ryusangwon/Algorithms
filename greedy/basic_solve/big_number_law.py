n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=True)

sum = 0
count = 0

while count != m:
    for i in range(k):
        sum += arr[0]
        count += 1
    sum += arr[1]
    count += 1

print(sum)