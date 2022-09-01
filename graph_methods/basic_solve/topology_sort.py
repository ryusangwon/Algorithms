"""
indegree: the number of edges into node
1. put the node with indegree 0 into queue
2. pop the node from queue and eliminate the edge which starts from that node
3. put the node which newly become indegree 0 into the queue

when queue is empty while not visited to all of the nodes, it means there are cycle
"""

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(result)

topology_sort()
