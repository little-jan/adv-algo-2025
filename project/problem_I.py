from collections import deque, defaultdict


def checker(adjlist, letters, num_places):
    if letters[0] != letters[-1]:
        print("Impossible")
        return

    u_to_s = [defaultdict(list) for _ in range(num_places + 1)]
    s_to_v = [defaultdict(list) for _ in range(num_places + 1)]

    for i in range(1, num_places + 1):
        for adj in adjlist[i]:
            u_to_s[i][letters[adj - 1]].append(adj)
            s_to_v[adj][letters[i - 1]].append(i)

    start = (1, num_places)
    visited = {start}
    parent = {}

    q = deque([start])
    terminating_center = None
    even_length = False

    while q:
        u, v = q.popleft()

        if u == v:
            terminating_center = (u, v)
            even_length = False
            break

        if v in adjlist[u]:
            terminating_center = (u, v)
            even_length = True
            break

        common_labels = set(u_to_s[u].keys()) & set(s_to_v[v].keys())

        for ch in common_labels:
            for s_u in u_to_s[u][ch]:
                for s_v in s_to_v[v][ch]:
                    s = (s_u, s_v)
                    if s not in visited:
                        visited.add(s)
                        parent[s] = (u, v)
                        q.append(s)

    if terminating_center is None:
        print("Impossible")
        return

    path = []
    current = terminating_center
    while True:
        path.append(current)
        if current == start:
            break
        current = parent[current]
    path.reverse()

    final = [u for (u, _) in path]
    if even_length:
        final.append(path[-1][1])
    final += [v for (_, v) in reversed(path[:-1])]

    print("Possible")
    print(len(final))
    print(" ".join(map(str, final)))


num_places, num_edges = map(int, input().split())
letters = input().split()

adjlist = [[] for _ in range(num_places + 1)]
for i in range(num_edges):
    u, v = map(int, input().split())
    adjlist[u].append(v)

checker(adjlist, letters, num_places)