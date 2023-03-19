from egzP4btesty import runtests 

class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None

def nastempnik(root):

    if root.right:
      
      root = root.right

      while root.left != None:
        root = root.left
      return root
    
    else:
      p_root = root.parent
      while p_root != None:
        if root == p_root.left:
          break
        
        root = p_root
        p_root = p_root.parent
      
      return p_root

def poprzednik(root):

    if root.left:
      
      root = root.left

      while root.right != None:
        root = root.right
      return root
    
    else:
      p_root = root.parent
      while p_root != None:
        if root == p_root.right:
          break
        
        root = p_root
        p_root = p_root.parent
      
      return p_root

    
def find(root,T):
  suma = 0
  for ver in T:
    nas = nastempnik(ver)
    pop = poprzednik(ver)

    if nas and pop:
      if ver.key == (nas.key + pop.key) / 2:
        suma += ver.key
  
  return suma



def sol(root, T):

    return find(root, T)
    
runtests(sol, all_tests = True)