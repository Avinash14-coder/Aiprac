from collections import deque
graph={
    0:[1,2],
    1:[0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

visited=set()
q=deque([0])
visited.add(0)

while q:
    node=q.popleft()
    print(node," ")

    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            q.append(n)