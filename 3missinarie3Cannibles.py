import heapq

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def valid(m, c):
    mr = 3 - m
    cr = 3 - c

    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False

    if m > 0 and c > m:
        return False

    if mr > 0 and cr > mr:
        return False

    return True

def heuristic(state):
    m, c, boat = state
    return (m + c + 1) // 2

def neighbors(state):
    m, c, boat = state
    result = []

    for dm, dc in moves:
        if boat == 0:
            nm, nc = m - dm, c - dc

            if dm <= m and dc <= c and valid(nm, nc):
                result.append((nm, nc, 1))
        else:
            nm, nc = m + dm, c + dc

            if dm <= 3 - m and dc <= 3 - c and valid(nm, nc):
                result.append((nm, nc, 0))

    return result

def a_star(start, goal):
    queue = [(heuristic(start), 0, start)]
    cost = {start: 0}
    parent = {start: None}

    while queue:
        f, g, current = heapq.heappop(queue)

        if g != cost[current]:
            continue

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for nxt in neighbors(current):
            new_cost = g + 1

            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                parent[nxt] = current

                heapq.heappush(
                    queue,
                    (new_cost + heuristic(nxt), new_cost, nxt)
                )

    return None

start = (3, 3, 0)
goal = (0, 0, 1)

path = a_star(start, goal)

if path:
    print("Solution using A* Algorithm\n")

    for i, (m, c, boat) in enumerate(path):
        side = "Left" if boat == 0 else "Right"
        print(f"Step {i}: M={m}, C={c}, Boat={side}")

    print("\nTotal crossings:", len(path) - 1)
else:
    print("No solution found")