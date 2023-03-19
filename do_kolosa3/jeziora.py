
from collections import deque
from queue import PriorityQueue


def DFS(G,visited,i,j,row,col):

    visited[i][j] = True

    if j+1 < col and not visited[i][j+1] and G[i][j+1] == 1:
        DFS(G,visited,i,j+1,row,col)
    
    if j-1 > -1 and not visited[i][j-1] and G[i][j-1] == 1:
        DFS(G,visited,i,j-1,row,col)
    
    if i+1 < row and not visited[i+1][j] and G[i+1][j] == 1:
        DFS(G,visited,i+1,j,row,col)
    
    if i-1 > -1 and not visited[i-1][j] and G[i-1][j] == 1:
        DFS(G,visited,i-1,j,row,col)

def BFS_path(G,row,col):
          pass

def ile_jezior(G):
    row = len(G)
    col =  len(G[0])
    visited = [[False for i in range(col)] for j in range(row)]

    lakes = 0
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and G[i][j] == 1:
                DFS(G,visited,i,j,row,col)
                lakes += 1
    
    return lakes


G = [
  [0,0,1,0,0,0,0,0,0,0],          
  [0,1,1,1,0,0,0,0,0,0],          
  [0,0,1,1,0,0,0,1,1,0],          
  [0,0,1,0,0,0,0,0,1,0],          
  [0,0,0,0,1,1,1,1,0,0],          
  [0,0,0,0,1,0,0,0,0,0],          
]
graph = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        ]

print(ile_jezior(graph))