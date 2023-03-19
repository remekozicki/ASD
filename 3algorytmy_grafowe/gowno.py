
from collections import deque


q = deque()

for i in range(10-1,-1,-1):
    q.append(i)

sorted(q[0])
print(q)