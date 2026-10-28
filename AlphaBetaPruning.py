import matplotlib.pyplot as plt
import networkx as nx

tree = nx.DiGraph()

edges = [
    ("A", "B"), ("A", "C"),
    ("B", "D"), ("B", "E"),
    ("C", "F"), ("C", "G")
]

tree.add_edges_from(edges)

values = {
    "A": "MAX",
    "B": "MIN",
    "C": "MIN",
    "D": "3",
    "E": "5",
    "F": "2",
    "G": "9"
}

pos = {
    "A": (0, 3),
    "B": (-1, 2),
    "C": (1, 2),
    "D": (-1.5, 1),
    "E": (-0.5, 1),
    "F": (0.5, 1),
    "G": (1.5, 1)
}

alpha = float('-inf')
beta = float('inf')

print("Alpha-Beta Pruning")
print("A is MAX, B and C are MIN\n")

b_value = min(3, 5)
alpha = max(alpha, b_value)

print("B = min(3, 5) =", b_value)
print("Alpha at A =", alpha)

f_value = 2
beta = min(beta, f_value)

print("\nC examines F =", f_value)
print("Beta at C =", beta)

if alpha >= beta:
    print("Pruning G =", 9)
    values["G"] = "9 PRUNED"
else:
    beta = min(beta, 9)

a_value = max(b_value, f_value)

print("\nFinal value at A =", a_value)
print("Best value for MAX =", a_value)

colors = []
for node in tree.nodes():
    if node == "G":
        colors.append("red")
    elif node in ["D", "E", "F"]:
        colors.append("lightgreen")
    else:
        colors.append("skyblue")

nx.draw(
    tree,
    pos,
    labels=values,
    with_labels=True,
    node_color=colors,
    node_size=2200,
    font_size=12,
    font_weight="bold",
    arrows=True
)

plt.title("Alpha-Beta Pruning Game Tree")
plt.text(1.1, 0.6, "G is pruned\n(alpha >= beta)", color="red",
         fontsize=10, ha="center")
plt.axis("off")
plt.show()