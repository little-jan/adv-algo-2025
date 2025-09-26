from heapq import *
from collections import deque

def tree_maker(lst):
    children = {}

    for i, manager in enumerate(lst):
        child_id = i + 2
        if manager not in children:
            children[manager] = [child_id]
        else:
            children[manager].append(child_id)
    return children

def dijkstras(adj_dict, src):
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
rankings, pred = dijkstras(children, 1)

reversed_rankings = sorted(rankings.items(), key = lambda x:x[1], reverse = True)
trained = 0
covered = [False for _ in range(num_employees + 1)]

for employee_keyvalue in reversed_rankings:
    employee = employee_keyvalue[0]
    if not covered[employee]:
        manager_to_train = employee

        for _ in range(distance):
            if manager_to_train == 1 or manager_to_train not in pred:
                break
            manager_to_train = pred[manager_to_train]

        trained += 1

        coverage_q = deque([(manager_to_train, 0)])
        covered[manager_to_train] = True

        while coverage_q:
            current_employee, dist = coverage_q.popleft()

            if dist >= distance:
                continue

            if current_employee in children:
                for child in children[current_employee]:
                    if not covered[child]:
                        covered[child] = True
                        coverage_q.append((child, dist + 1))

print(trained)