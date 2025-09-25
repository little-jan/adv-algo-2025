def tree_maker(lst, num_employees):
    children = {}
    for child in range(num_employees):
        parent = lst[child]
        if parent not in children:
            children[parent] = [child]
        else:
            children[parent].append(child)
    return children

def ranking(children, num_employees):
    rankings = [0] * num_employees

    def dfs(node, depth):
        rankings[node] = depth
        if node in children:
            for child in children[node]:
                dfs(child, depth + 1)

    dfs(1, 1)  # start at root=1 with depth=1

    for i in range(num_employees):
        if rankings[i] == 0:
            dfs(i, 2)

    return rankings

num_employees, distance = map(int, input().split())
lst = list(map(int, input().split()))
children = tree_maker(lst, num_employees)
rankings = ranking(children, num_employees)

print(children)
print(rankings)
