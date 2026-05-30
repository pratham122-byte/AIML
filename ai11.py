#a*
parent=(start:None)
print("\n a* traversal steps")
while open_list:
    current=min(open_list,key=lambda X:g[x] +h[x])
    print("\n current node:",current)

for neighbour  in graph[current]:
    cost=graph[current][neighbour]
    if neighbour in closed_list:
        continue
    new_g =g[current]+cost
    if neighbour not in open_list:
        open_list.append(neighbour)
    if new_g<g[neighbour]:
        g[neighbour]=new_g
        parent[neighbour]=current
path=[]
node=global
while node is not None:
    path.append(node)
    node=parent.get(node,None)
path.reverse()
print("\n final a* path:","->".join(path))
print("\n total cost=",g[goal])