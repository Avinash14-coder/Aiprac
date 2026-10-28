blocks = ['A', 'B', 'C']
goal = ['A', 'B', 'C']

def heuristic(state):
    score = 0
    for i in range(len(state)):
        if state[i] == goal[i]:
            score += 1
    return score

state = ['C', 'B', 'A']

while state != goal:
    print("Current state:", state)
    best = state[:]

    for i in range(len(state)):
        new_state = state[:]
        new_state[i], new_state[(i + 1) % len(state)] = new_state[(i + 1) % len(state)], new_state[i]

        if heuristic(new_state) > heuristic(best):
            best = new_state

    if heuristic(best) <= heuristic(state):
        print("Local maximum reached")
        break

    state = best

print("Final state:", state)