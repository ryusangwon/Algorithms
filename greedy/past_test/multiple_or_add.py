arr = list(map(int, input()))

sum = 1
for i in arr:
    if i is not 0:
        sum *= i

print(sum)