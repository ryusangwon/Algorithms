# binary search & parametric search -> don't use recursive in parametric search

n, m = map(int, input().split())    # 1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += (x - mid)

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)