def tree_maker(lst):
    children = {}

    for i, manager in enumerate(lst):
        child_id = i + 2
        if manager not in children:
            children[manager] = [child_id]
        else:
            children[manager].append(child_id)
    return children

def ranker(children, num_employees):
    rankings = [None] * (num_employees + 1)

    rankings[1] = 0

    def dfs(employee):
        if employee in children:
            for child in children[employee]:
                if rankings[child] is None:
                    rankings[child] = rankings[employee] + 1
                    dfs(child)

    dfs(1)
    return rankings

num_employees, distance = map(int, input().split())
lst = list(map(int, input().split()))
children = tree_maker(lst)
rankings = ranker(children, num_employees)

trained = 1

for i in range(len(rankings)):
    rank = rankings[i]

    if rank is None or rank == 0:
        continue

    else:
        if rank % distance == 0 and children.get(i):
            trained += 1

print(trained)