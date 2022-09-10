def solution(food_times, k):
    answer = 0
    for i in range(2000):
        index = i % len(food_times)
        if k == 0:
            break
        if food_times[index] != 0:
            food_times[index] -= 1
            answer = index + 1
            if answer == 3:
                answer = 0
            k -= 1
    print(food_times)
    return answer

k = int(input())
food_times = list(map(int, input().split()))
print(solution(food_times, k))
