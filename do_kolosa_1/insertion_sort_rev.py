def insertion_sort(A):
    for i in range(len(A)):
        X = A[i]
        j = i - 1
        while j >= 0 and A[j] > X:
            A[j+1] = A[j]
            j -= 1
        A[j+1] =  X 

tab = [2,1,4,3,6,5,7,8]
insertion_sort(tab)
print(tab)