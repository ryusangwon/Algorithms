n, m = map(int, input().split())

result = 0

for i in range(m):
    arr = list(map(int, input().split()))
    arr_min = min(arr)
    result = max(result, arr_min)

print(result)