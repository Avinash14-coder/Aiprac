graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 5, 'E': 2},
    'C': {'F': 3},
    'D': {'F': 2},
    'E': {'F': 2},
    'F': {}
}

h = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 2, 'F': 0}

open_list = [(h['A'], 0, 'A')]
cost = {'A': 0}
parent = {}

while open_list:
    open_list.sort()
    f, g, node = open_list.pop(0)

    if g != cost[node]:
        continue

    if node == 'F':
        break

    for neighbor, weight in graph[node].items():
        new_cost = g + weight

        if neighbor not in cost or new_cost < cost[neighbor]:
            cost[neighbor] = new_cost
            parent[neighbor] = node
            open_list.append((new_cost + h[neighbor], new_cost, neighbor))

if 'F' in cost:
    path = []

    while node in parent:
        path.append(node)
        node = parent[node]

    path.append('A')
    path.reverse()

    print("Minimum cost path:", path)
    print("Minimum cost:", cost['F'])
else:
    print("Goal node not reachable")