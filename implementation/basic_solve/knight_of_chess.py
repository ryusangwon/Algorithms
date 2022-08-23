
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
length = len(dx)
a = list(input())
x = ord(a[0]) - 96
y = int(a[1])

count = 0

for i in range(length):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx >= (length-1) or ny < 1 or ny >= (length-1):
        continue
    count += 1

print(count)