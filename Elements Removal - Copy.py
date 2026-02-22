#Given an integer array A of size N. In one operation, you can remove any element from the array, and the cost of this operation is the sum of all elements in the array present before this operation.
#Find the minimum cost to remove all elements from the array.

def solve(A):
    A.sort()
    n=len(A)
    sum1=0
    for i in range(len(A)):
        sum1=sum1+(A[i]*n)
        n-=1
    return sum1