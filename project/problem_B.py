def dfs_postorder(adjlist, visited, root):
    postorder = []
    def dfs(current):
        if not visited[current]:
            visited[current] = True
            for neighbor in reversed(adjlist[current]):
                dfs(neighbor)
            postorder.append(current)
    dfs(root)
    return postorder

def tranpose(adjlist):
    n = len(adjlist)
    result = [[] for _ in range(n)]
    for u in range(n):
        for v in adjlist[u]:
            if v >= n:
                result.extend([[] for _ in range(v - n + 1)])
                n = len(result)
            result[v].append(u)
    return result

def kosarajus(adjlist):
    postorder = []
    visited = [False for _ in adjlist]
    for i in range(1, len(adjlist)):
        if not visited[i]:
            postorder.extend(dfs_postorder(adjlist, visited, i))
    adjlist = tranpose(adjlist)
    visited = [False for _ in adjlist]
    sccs = []
    for i in reversed(postorder):
        if not visited[i]:
            sccs.append(dfs_postorder(adjlist, visited, i))
    return sccs

num_vertices, num_edges = map(int, input().split())
vertices = [int(input()) for _ in range(num_vertices)]
adjlist = [[] for _ in range(num_vertices + 1)]
for _ in range(num_edges):
    src, v = map(int, input().split())
    adjlist[src].append(v)

sccs = kosarajus(adjlist)
print(sccs)

friend_costs = [0 for _ in range(num_vertices + 1)]
visited = []
for i in sccs:   # i is a cycle
    if len(i) == 1:
        current = i
        weight = vertices[i]
        visited.append()

print(friend_costs)