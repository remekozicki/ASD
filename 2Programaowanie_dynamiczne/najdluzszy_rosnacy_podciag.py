# f(i) = max( f(j)+1 | j < i and A[j] < A[i])

# def find(T):
#     n = len(T)
#     F = [1 for i in range(n)]
#     # P = [-1 for i in range(n)]
#     max_i = 0
#     for i in range(1,n):
#         for j in range(0,i):
#             if T[i] > T[j]:
#                 F[i] = max(F[i],F[j]+1)
#                 # if F[j]+1 > F[i]:
#                 #     F[i] = F[j] + 1
#                 #     P[i] = j
#         if F[i] > F[max_i]:
#             max_i = i
    
#     # return max_i, F, P
#     return F[max_i]


def print_sol(i,T,P):

    if P[i] != -1:
        print_sol(P[i],T,P)
    print(T[i])



def find(T):

    n = len(T)

    F = [1 for i in range(n)]
    parents = [None for i in range(n)]

    for i in range(n):
        for j in range(i):

            if T[i] > T[j]:

                if F[i] < F[j]+1:
                    F[i] = F[j]+1
                    parents[i] = j
    
    return F,parents




t = [2,1,4,3,4,8,5,7,2,0]
f,p = find(t)
print(f)
print(p)
# max_i, F, P = find(t)
# print(F[max_i])
# print_sol(max_i,t,P)