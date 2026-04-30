n = 4

names = ["P0","P1","P2","P3"]

graph ={
    0: [1],
    1: [2],
    2: [0,3],
    3: [2]
}

def dfs(v,visited, stack):
    visited[v]=True
    for nei in graph[v]:
        if not visited[nei]:
            dfs(nei, visited, stack)
    stack.append(v)

def reverse_graph():
    rev = {i: [] for i in range(n)}
    for u in graph:
        for v in graph[u]:
            rev[v].append(u)
    return rev

def dfs_rev(v, visited, component, rev):
    visited[v] = True
    component.append(v)
    for nei in rev[v]:
        if not visited[nei]:
            dfs_rev(nei, visited, component, rev)


visited= [False] * n
stack = []

for i in range(n):
    if not visited[i]:
        dfs(i, visited , stack)

rev = reverse_graph()
visited = [False] * n

deadlock = False

print("Strongly Connected Components :")

while stack:
    node = stack.pop()
    if not visited[node]:
        comp = []
        dfs_rev(node,visited,comp, rev)

        processes = [names[i] for i in comp]
        print(processes)

        if len(comp) > 1:
            deadlock = True
            print("\nDeadlock Detected among :", processes)

if not deadlock:
    print("No Deadlock")