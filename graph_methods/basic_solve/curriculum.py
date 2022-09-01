"""
topology sort
"""
import copy
from collections import deque

n = int(input())
indegree = [0] * (n+1)
score = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    score[i] = data[0]
    for j in data[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    q = deque()
    result = copy.deepcopy(score)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + score[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()