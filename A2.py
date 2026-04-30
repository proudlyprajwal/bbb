import heapq

def dijkstra():

    n = int(input("Enter number of buildings: "))
    buildings = []

    print("Enter building names:")
    for _ in range(n):
        buildings.append(input().strip())

    e = int(input("Enter number of walkways: "))
    walkways = []

    print("Enter walkways (Building1 Building2 Distance):")
    for _ in range(e):
        u, v, w = input().split()
        walkways.append((u, v, int(w)))

    source = input("Enter source building (Main Gate): ")


    graph = {b: [] for b in buildings}
    for u, v, w in walkways:
        graph[u].append((v, w))
        graph[v].append((u, w))   # Undirected graph


    distance = {b: float('inf') for b in buildings}
    distance[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))


    print("\nShortest walking distances from", source)
    for b in buildings:
        print(source, "->", b, "=", distance[b])

dijkstra()