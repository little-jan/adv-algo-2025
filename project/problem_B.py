def transpose(edges):
    n = len(edges)
    result = []

    for u in reversed(range(n)):
        src, v = edges[u]
        result.append((v, src))

    return result


num_vertices, num_edges = map(int, input().split())

vertices = []
for i in range(num_vertices):
    vertices.append(int(input()))

edges = []
for i in range(num_edges):
    src, v = map(int, input().split())
    edges.append((src, v))

friend_costs = [0 for _ in range(num_vertices + 1)]
seen = [False for _ in range(num_vertices + 1)]
visited = [False for _ in range(num_vertices + 1)]

transposed = transpose(edges)

for edge in transposed:
    src, v = edge
    friend_costs[v] = max(friend_costs[src], vertices[src-1])

for val in friend_costs[1:]:
    print(val)