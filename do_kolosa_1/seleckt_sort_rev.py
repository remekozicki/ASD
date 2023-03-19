def select_sort(A):
    
    for i in range(len(A)-1):
        key  = i
        
        for j in range(i,len(A)):
            
            if A[key] > A[j]:
                key = j
        
        A[i], A[key] = A[key], A[i]

tab = [2,1,4,3,6,5,7,8]
select_sort(tab)
print(tab)