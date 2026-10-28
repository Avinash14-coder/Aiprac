from heapq import heappush, heappop

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return distance

pq = []
heappush(pq, (h(start), 0, start, []))
visited = set()

while pq:
    f, g, state, path = heappop(pq)

    if state in visited:
        continue

    visited.add(state)
    path = path + [state]

    if state == goal:
        for s in path:
            print(s[:3])
            print(s[3:6])
            print(s[6:])
            print()
        print("Steps:", len(path) - 1)
        break

    z = state.index(0)
    r, c = z // 3, z % 3

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc
            new = list(state)
            new[z], new[nz] = new[nz], new[z]
            new = tuple(new)

            if new not in visited:
                heappush(pq, (g + 1 + h(new), g + 1, new, path))