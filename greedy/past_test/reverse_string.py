arr = list(map(int, input()))

zero_count = 0
one_count = 0


if arr[0] == 0:
    zero_count += 1
else:
    one_count += 1

for i in range(len(arr) - 1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == 0:
            zero_count += 1
        else:
            one_count += 1

print(min(zero_count, one_count))