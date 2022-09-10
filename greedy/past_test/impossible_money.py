n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum = 1
for i in range(len(arr)):
    sum += arr[i]
    if sum < arr[i+1]:
        break
print(sum)
