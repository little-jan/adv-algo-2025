from collections import deque

def bfs(src, target):
    q = deque()
    visited = {tuple(src): True}
    q.append((tuple(src), 0))

    while q:
        current = q.popleft()
        compare = converter(current[0])
        if compare == target:
            return current[1]

        for node in switcher(list(current[0])):
            if tuple(node) not in visited:
                visited[tuple(node)] = True
                q.append((tuple(node), current[1] + 1))
    return -1

def converter(lst):
    newlst = []
    newlen = len(lst) - 2
    for i in range(newlen):
        if lst[i] != 'E':
            newlst.append(lst[i])
    string = ''.join(newlst)
    return string

def switcher(parsed):
    adj = []
    empty = [i for i, c in enumerate(parsed) if c == 'E']

    for i in range(len(parsed) - 1):
        if parsed[i] != 'E' and parsed[i + 1] != 'E':
            parsedcopy = parsed.copy()
            e1, e2 = empty
            parsedcopy[e1], parsedcopy[e2] = parsedcopy[i], parsedcopy[i + 1]
            parsedcopy[i], parsedcopy[i + 1] = 'E', 'E'
            adj.append(parsedcopy)
    return adj


length = input()
src = input()
target = input()

parsed = []
for char in src:
    parsed.append(char)
parsed.append('E')
parsed.append('E')

print(bfs(parsed, target))