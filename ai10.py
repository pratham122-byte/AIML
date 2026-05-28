n = int(input("Enter number of nodes: "))
nodes = []

print("Enter node names:")
for i in range(n):
    name = input(f"Node {i+1} name: ")
    nodes.append(name)

graph = {}

print("\nEnter neighbours and cost for each node (format: A 3 B 5)")
print("Press enter if no neighbour.")

for node in nodes:
    entry = input(f"Neighbours of {node}: ").split()
    neighbours = {}
    for i in range(0, len(entry), 2):
        neighbour = entry[i]
        cost = int(entry[i+1])
        neighbours[neighbour] = cost
    graph[node] = neighbours

h = {}
print("\nEnter heuristic values:")
for node in nodes:
    val = int(input(f"h({node}) = "))
    h[node] = val

print("\nGraph:", graph)
print("Heuristic:", h)