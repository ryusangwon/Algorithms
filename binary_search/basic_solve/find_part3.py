import time

start_time = time.time()
n = int(input())
array = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
end_time = time.time()
print("list time:", end_time-start_time)

start_time = time.time()
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

end_time = time.time()
print("set time:", end_time-start_time)