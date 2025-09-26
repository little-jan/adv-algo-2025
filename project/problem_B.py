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
    for u in range(1, n):
        for v in adjlist[u]:
            result[v].append(u)
    return result


def kosarajus(adjlist):
    visited = [False for _ in adjlist]
    postorder = []
    for i in range(1, len(adjlist)):
        if not visited[i]:
            postorder.extend(dfs_postorder(adjlist, visited, i))

    adjlist = tranpose(adjlist)

    for i in range(len(visited)):
        visited[i] = False

    sccs = []
    for i in reversed(postorder):
        if not visited[i]:
            sccs.append(dfs_postorder(adjlist, visited, i))
    return sccs


def scc_processing(sccs, num_vertices):
    scc_groups = [0 for _ in range(num_vertices + 1)]
    for i in range(len(sccs)):
        for vertex in sccs[i]:
            scc_groups[vertex] = i

    scc_maximums = []
    for i in range(len_sccs):
        scc = sccs[i]
        max1, max2 = 0, 0
        for vertex in scc:
            cost = vertex_weights[vertex]
            if cost > max1:
                max2 = max1
                max1 = cost
            elif max1 > cost > max2:
                max2 = cost
        scc_maximums.append((max1, max2, len(scc)))

    scc_dag = [[] for _ in range(len(sccs))]
    for u in range(1, num_vertices + 1):
        for v in adj[u]:
            if scc_groups[u] != scc_groups[v]:
                scc_dag[scc_groups[u]].append(scc_groups[v])

    return scc_groups, scc_maximums, scc_dag


num_vertices, num_edges = map(int, input().split())

vertex_weights = [0]
for i in range(num_vertices):
    vertex_weights.append(int(input()))

adj = [[] for _ in range(num_vertices + 1)]
for i in range(num_edges):
    u, v = map(int, input().split())
    adj[u].append(v)


sccs = kosarajus(adj)
len_sccs = len(sccs)

scc_groups, scc_maximums, scc_dag = scc_processing(sccs, num_vertices)

dp = [x[0] for x in scc_maximums]
for i in reversed(range(len_sccs)):
    for neighbouring_scc in scc_dag[i]:
        dp[i] = max(dp[i], dp[neighbouring_scc])

friendship_costs = [0 for _ in range(num_vertices + 1)]
for i in range(1, num_vertices + 1):
    scc_group = scc_groups[i]
    v_cost = vertex_weights[i]
    max_reachable = dp[scc_group]

    if v_cost < max_reachable:
        friendship_costs[i] = max_reachable
    else:
        max_cost = 0
        for neighbor_scc in scc_dag[scc_group]:
            max_cost = max(max_cost, dp[neighbor_scc])

        scnd_max_cost = scc_maximums[scc_group][1]
        friendship_costs[i] = max(scnd_max_cost, max_cost)

for val in friendship_costs[1:]:
    print(val)
