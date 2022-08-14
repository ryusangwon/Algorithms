n = int(input())

# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], input_data[1]))
#
# array = sorted(array, key=lambda student: student[1])
#
# for student in array:
#     print(student[0], end=' ')

dict = {}
for i in range(n):
    input_data = input().split()
    dict[input_data[0]] = input_data[1]

dict = sorted(dict.items(), reverse=True)

for student in dict:
    print(student[0], end=' ')