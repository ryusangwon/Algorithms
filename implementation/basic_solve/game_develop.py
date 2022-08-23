n, m = map(int, input().split())

x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]

d[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction += 1
    if direction == len(d) - 1:
        direction = 0

count = 1
turn_time = 0
while True:

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or nx > (len(d) - 1) or ny < 0 or ny > (len(d) - 1):
        print("no way")
        break

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)