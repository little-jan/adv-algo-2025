from collections import deque

def tranpose(adjlist):
    result = [[] for _ in adjlist]
    for u in range(len(adjlist)):
        for v in adjlist[u]:
            result[v].append(u)
    return result

def checker(adjlist, letters, num_places, num_edges):
    if letters[0] == letters[-1]:
        no = "Impossible"
        length = None
        indexes = None
        return no, length, indexes
    else:
        transposed_adjlist = tranpose(adjlist)
        s_adjlist = 1
        q_adjlist = deque()
        s_tranposed = num_places
        q_tranposed = deque()
        visited_adjlist = [False] * num_places + 1
        visited_tranposed = [False] * num_places + 1

        visited_adjlist[s_adjlist] = True
        q_adjlist.append(s_adjlist)
        visited_tranposed[s_tranposed] = True
        q_tranposed.append(s_tranposed)

        while q_tranposed and q_adjlist:
            curr_adjlist = q_adjlist.popleft()
            curr_tranposed = q_tranposed.popleft()




num_places, num_edges = map(int, input().split())
letters = input().split()

adjlist = [[] for _ in range(num_edges + 1)]
for i in range(num_edges):
    u, v = map(int, input().split())
    adjlist[u].append(v)

