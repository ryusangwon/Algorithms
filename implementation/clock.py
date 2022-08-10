n = int(input())

count = 0
if 0 <= n < 24:
    for i in range(n + 1):  # caution
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

else:
    print("invalid number")

print(count)