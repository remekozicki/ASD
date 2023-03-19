from kol3atesty import runtests
from math import inf
from queue import PriorityQueue as PQ


def relax(distances, d, u, w):

    if distances[u] > d + w:
        distances[u] = d + w
        return True

    return False


def spacetravel(n, E, S, a, b):

    G = [[] for _ in range(n)]
    for u, v, w in E:
        G[u].append([v, w])
        G[v].append([u, w])

    visited = [False for _ in range(n)]
    distances = [inf for _ in range(n)]
    queue = PQ()

    queue.put((0, a))
    distances[a] = 0

    while not queue.empty():
        d, u = queue.get()

        if u == b:
            return d

        for v, w in G[u]:
            if not visited[v]:
                if relax(distances, d, v, w):
                    queue.put((d + w, v))

        if u in S:
            for v in S:
                if v != u and not visited[v]:
                    if relax(distances, d, v, 0):
                        queue.put((d, v))

        visited[u] = True

    return None


runtests(spacetravel, all_tests=True)