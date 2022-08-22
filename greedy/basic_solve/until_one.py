import time

start_time = time.time()
n, k = map(int, input().split())

count = 0
while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1  # substitute 1 in once

print(count)
end_time = time.time()
print(end_time-start_time)