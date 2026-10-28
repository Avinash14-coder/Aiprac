
initial = {
    "A": "Table",
    "B": "Table",
    "C": "Table",
    "D": "C"
}

goal = {
    "A": "B",
    "B": "D",
    "C": "Table",
    "D": "Table"
}

stack = []
plan = []

for block in goal:
    stack.append((block, goal[block]))

while stack:
    block, position = stack.pop()

    if initial[block] != position:
        plan.append(f"Move {block} from {initial[block]} to {position}")
        initial[block] = position

print("Goal Stack Planning")
print("\nPlan:")

for action in plan:
    print(action)

print("\nFinal State:")

for block, position in initial.items():
    print(block, "on", position)
