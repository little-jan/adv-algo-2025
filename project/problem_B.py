from collections import deque

num_vertices, num_edges = map(int, input().split())

vertex_weights = [0]
for i in range(num_vertices):
    vertex_weights.append(int(input()))

adj = [[] for _ in range(num_vertices + 1)]
for i in range(num_edges):
    u, v = map(int, input().split())
    adj[u].append(v)

friendship_costs = [0] * (num_vertices + 1)

for src in range(1, num_vertices + 1):

    q = deque([src])
    reachable_people = {src}

    while q:
        current = q.popleft()
        for neighbor in adj[current]:
            if neighbor not in reachable_people:
                reachable_people.add(neighbor)
                q.append(neighbor)

    max_reachable_cost = 0
    for person in reachable_people:
        if person != src:
            max_reachable_cost = max(max_reachable_cost, vertex_weights[person])

    friendship_costs[src] = max_reachable_cost

for val in friendship_costs[1:]:
    print(val)
