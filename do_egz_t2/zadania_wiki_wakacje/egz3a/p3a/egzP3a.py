from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None


def vote(T):
  m = len(T)

  votes = 0

  for i in range(m):
    wo = tmp = T[i]
    p = wo.fundusze
    n = 0
    while tmp != None:
      tmp = tmp.next
      n += 1
    
    DP = [[None for i in range(p+1)] for i in range(n)]
    votes += rec(wo,p,DP,idx = 0)
  
  return votes


def rec(wo,p,DP,idx):

  if wo == None or p == 0:
    return 0

  if DP[idx][p] != None:
    return DP[idx][p]
  
  if wo.koszt <= p:
    DP[idx][p] = max(wo.wyborcy + rec(wo.next,p - wo.koszt,DP,idx + 1), rec(wo.next,p,DP,idx+1))
    return DP[idx][p]
  
  elif wo.koszt > p:
    DP[idx][p] = rec(wo.next, p, DP, idx+1)
    return DP[idx][p]

def wybory(T):
    #tutaj proszę wpisać własną implementację
    return vote(T)

runtests(wybory, all_tests = True)