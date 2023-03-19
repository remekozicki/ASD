from cmath import inf


def insertion_sort(T):

    for i in range(len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j] > X:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X


def counting_sort(P):
    n = len(P)
    max_val = 0
    min_val = float("inf")
    for i in range(n):
        if P[i][0] < min_val:
            min_val = P[i][0]
        if P[i][0] > max_val:
            max_val = P[i][0]
    
    end_val = max_val - min_val + 1 

    C = [0]*(end_val)

    for i in P:
        C[i[0] - min_val] += 1
    
    for i in range(1,end_val):
        C[i] = C[i-1] + C[i]
    
    result = [0]*n

    for i in range(n-1,-1,-1):
        result[C [ P[i][0] - min_val ] - 1] = P[i]
        C[P[i][0]-min_val] -= 1
    
    return result


    

def merge_ranges(P):
    i = 0
    while i < len(P)-1:
        if P[i][2] == 0:
            P = P[:(i)] + P[i:]
            i+=1
            if P[i][1] >= P[i+1][0]:
                f = min(P[i][0],P[i+1][0])
                b = max(P[i+1][1],P[i][1])
                n = P[i][2] + P[i+1][2]
                new_el = (f,b,n)
                P[i-1] = new_el
                P = P[:(i)] + P[i+1:]
                
            else:
                i += 1
    return P
    

def bucket_sort(A,P):
    
    n = len(A)
    max_val = P[1]
    min_val = P[0]
    prob = P[2]
    buckets = [[] for _ in range(int(prob * n)+1)]

    for i in range(n):
        if A[i] != -1:
            index = int(((A[i] - min_val) / (max_val - min_val))*n)
            if index >= (max_val + 1):
                continue
            else:
                buckets[index].append(A[i])
                A[i] = -1

    for j in range(len(buckets)):
        insertion_sort(buckets[j])
    
    result = []

    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            result.append(buckets[i][j])
    
    
    return result



def SortTab(A,P):
    to_return = []
    P = counting_sort(P)
    P  = merge_ranges(P)
    for i in range(len(P)):
        to_return = to_return + bucket_sort(A,P[i])
    
    return to_return






P = [(1, 5, 0.0), (4, 8, 0.25), (5, 8, 0.000), (6, 7, 0.1), (34, 65, 0.1), (3, 5, 0.2)]
T = [ 1.5, 4.3, 2.7, 3.8, 6.9, 7.3, 7.9, 35.5, 59.8]

SortTab(T,P)