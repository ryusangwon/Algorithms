# binary search using recursive

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("No number")
else:
    print(result + 1)