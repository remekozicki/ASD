
# MST
from queue import PriorityQueue

def prim(G):

    n = len(G)
    queue = PriorityQueue()
    visited = [False] * n
    parents = [None] * n
    putted = [False] * n
    state = [None] * n

    queue.put([0, 0])
    putted[0] = True

    while not queue.empty():
        x = queue.get()

        if not visited[x[1]]:

            for u in G[x[1]]:
                if not putted[u[0]]:
                    queue.put([u[1], u[0]])
                    putted[u[0]] = True
                    parents[u[0]] = x[1]
                    state[u[0]] = u[1]
                else:
                    if not visited[u[0]]:
                        queue.put([u[1], u[0]])
                        if state[u[0]] > u[1]:
                            parents[u[0]] = x[1]
                            state[u[0]] = u[1]

        visited[x[1]] = True
    
    # return parents

    ans = []
    for i in range(1, n):
        ans.append(sorted([i, parents[i]]))

    return ans


graph = [[(1, 1), (2, 3)], [(0, 1), (3, 2), (4, 4)], [(0, 3), (3, 1), (4, 2)], [(1, 2), (2, 1), (5, 1)],
         [(1, 4), (2, 2), (5, 3)], [(3, 1), (4, 3)]]


print(prim(graph))