# 1 number of coin used
N = int(input())
count = 0
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += N // coin
    N %= coin
print("used coin number:", count)

# 2 big number law
## 1st answer
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m==0:
            break
        result += first
        m -= 1
    if m==0:
        break
    result += second
    m -= 1
print(result)

## 2nd answer
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1) * k) + m % (k+1)
result = 0
result += count * first
result += (m-count) * second

print(result)

# 3 card game
## 1st answer
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

## 2nd answer
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)

# 4 until 1
## 1st answer
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1

    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

## 2nd answer
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)