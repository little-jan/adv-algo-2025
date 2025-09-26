from heapq import *

def tree_maker(lst):
    children = {}

    for i, manager in enumerate(lst):
        child_id = i + 2
        if manager not in children:
            children[manager] = [child_id]
        else:
            children[manager].append(child_id)
    return children


from heapq import *


def dijkstras(adj_dict, num_nodes, src):
    dist = {}
    pred = {}
    pq = []

    heappush(pq, (0, None, src))  # set is formatted (distance, predecessor, vertex)

    while pq:
        d, p, u = heappop(pq)
        if u in dist:
            continue
        dist[u] = d
        pred[u] = p

        if u in adj_dict:
            for child in adj_dict[u]:
                if child not in dist:
                    heappush(pq, (d + 1, u, child))

    return dist, pred

num_employees, distance = map(int, input().split())
lst = list(map(int, input().split()))
children = tree_maker(lst)
rankings, pred = dijkstras(children, num_employees, 1)

trained = 1

for i in range(1, len(rankings) + 1):
    rank = rankings.get(i)

    if rank == 0:
        continue

    else:
        if rank % distance == 0 and children.get(i):
            trained += 1

print(trained)