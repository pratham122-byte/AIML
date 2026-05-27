from collections import deque
def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]  
    while stack:
        path = stack.pop()  
        node = path[-1]      
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                new_path = path + [neighbor]
                stack.append(new_path)
    return None
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors
start = input("Enter start state: ")
goal = input("Enter goal state: ")
path = dfs(graph, start, goal)
print("DFS path found:", path)
