#You are given an integer array A of length N.
#You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
#For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
#More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
# A = [1, 2, 3, 4, 5]
# B = [[1, 4], [2, 3]]
# output [10,5]

def rangeSum(A, B):
    LR=[None] * len(A)
    RT=[]
    for i in range(len(A)):
        if i==0:
            LR[i]=A[i]
        else:
            LR[i]=LR[i-1]+A[i]
        
    print(LR)       
    for i in B:
        r,q=i
        r=r-1
        q=q-1
        print(r,q)
        if r==0:
            RT.append(LR[q])
        else:
            RT.append(LR[q] -LR[r-1])
    return RT