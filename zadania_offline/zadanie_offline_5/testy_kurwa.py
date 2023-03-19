from queue import PriorityQueue


q = PriorityQueue()

T = [[2,1],[5,4],[1,6],[3,3]]
for i in range(len(T)):
    q.put(T[i])

print(q.get())