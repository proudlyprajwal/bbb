INF = 999

nodes = ["A", "B", "C", "D"]

# Distance matrix
dist = [
    [0, 4, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

n = len(nodes)

def print_matrix():
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("∞", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()
    print()

print("Initial Distance Matrix:")
print_matrix()

# Floyd-Warshall Algorithm
for k in range(n):
    print("Intermediate Node:", nodes[k])

    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

    print("Updated Matrix:")
    print_matrix()

print("Final Shortest Distance Matrix:")
print_matrix()