graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

h = {'A': 5, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 0}

start = 'A'
goal = 'F'

open_list = [start]
visited = set()
parent = {}

while open_list:
    open_list.sort(key=lambda n: h[n])
    node = open_list.pop(0)

    if node in visited:
        continue

    visited.add(node)

    if node == goal:
        break

    for n in graph[node]:
        if n not in visited and n not in open_list:
            parent[n] = node
            open_list.append(n)

if node == goal:
    path = []

    while node in parent:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    print("Path:", path)
else:
    print("Goal not found")