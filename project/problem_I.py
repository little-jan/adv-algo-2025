from collections import deque, defaultdict



# ----- BFS code is inspired by https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/ -----

def bfs(adjlist, letters, num_places):
    forward_lst = [defaultdict(list) for _ in range(num_places + 1)]
    backward_lst = [defaultdict(list) for _ in range(num_places + 1)]

    for i in range(1, num_places + 1):
        for adj in adjlist[i]:
            forward_lst[i][letters[adj - 1]].append(adj)
            backward_lst[adj][letters[i - 1]].append(i)

    start = (1, num_places)
    visited = {start}
    parent = {}

    q = deque([start])
    terminating_center = None
    is_even = False

    while q:
        u, v = q.popleft()

        if u == v:
            terminating_center = (u, v)
            is_even = False
            break

        if v in adjlist[u]:
            terminating_center = (u, v)
            is_even = True
            break

        common_labels = set(forward_lst[u].keys()) & set(backward_lst[v].keys())

        for char in common_labels:
            for s_u in forward_lst[u][char]:
                for s_v in backward_lst[v][char]:
                    s = (s_u, s_v)
                    if s not in visited:
                        visited.add(s)
                        parent[s] = (u, v)
                        q.append(s)

    return terminating_center, is_even, parent


def checker(adjlist, letters, num_places):
    if letters[0] != letters[-1]:
        print("Impossible")
        return

    terminating_center, is_even, parent = bfs(adjlist, letters, num_places)

    if terminating_center is None:
        print("Impossible")
        return

    path = []
    current = terminating_center
    while True:
        path.append(current)
        if current == (1, num_places):
            break
        current = parent[current]
    path.reverse()

    final = [u for (u, _) in path]
    if is_even:
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