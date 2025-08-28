from collections import deque

def hascycle(adj):
    in_degree = [0] * len(adj)

    q = deque()
    visited = 0

    for u in range(len(adj)):
        for v in adj[u]:
            in_degree[v] += 1

    for u in range(len(adj)):
        if in_degree[u] == 0:
            q.append(u)

    while q:
        u = q.popleft()
        visited += 1

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    return visited != len(adj)

def toposort(adj):
    indegree = [0] * len(adj)
    for vs in adj:
        for v in vs:
            indegree[v] += 1
    sources = [u for u, d in enumerate(indegree) if d == 0]
    tpsort = []
    while len(sources) > 0:
        u = sources.pop()
        tpsort.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                sources.append(v)
    return tpsort

def longestpath(adj):
    dptable = [0] * len(adj)
    for u in reversed(toposort(adj)):
        if not adj[u]:
            dptable[u] = 0
        else:
            dptable[u] = max(dptable[v] for v in adj[u]) + 1

    high = 0
    for i in range(len(dptable)):
        if dptable[i] > high:
            high = dptable[i]

    return high + 1

flavours = int(input())
pairs = int(input())

adj = [[] for _ in range(flavours + 1)]

for i in range(pairs):
    line = input()
    line = line.split()
    u = int(line[0])
    v = int(line[1])
    adj[u].append(v)

if (hascycle(adj)):
    print(-1)
else:
    print(longestpath(adj))
