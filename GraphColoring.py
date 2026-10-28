graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors = [0] * 4
m = 3

def safe(node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve(node):
    if node == 4:
        return True

    for color in range(1, m + 1):
        if safe(node, color):
            colors[node] = color

            if solve(node + 1):
                return True

            colors[node] = 0

    return False

if solve(0):
    for i in range(4):
        print("Node", i, ":", "Color", colors[i])
else:
    print("No solution")