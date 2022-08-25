n = int(input())

array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))

print(array)
for i in array:
    print(i[0], end=' ')