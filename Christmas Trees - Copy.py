#You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
#The cost of these trees is Bp + Bq + Br.
#You are to choose 3 trees such that their total cost is minimum. Return that cost.
#If it is not possible to choose 3 such trees return -1.
# Input 1 : A = [1, 3, 5], B = [1, 2, 3]
# Input 2 : B =  A = [1, 6, 4, 2, 6, 9], B = [2, 5, 7, 3, 2, 7]
# Output 1 =6 Output 2 =7
# In problem 2 cost can be 2 + 3 + 2 for Height 1,2,6 hence ans is 7


def Mincost(A,B):
    cost3=10**9
    n=len(A)
    for i in range(n):
        cost1=10**9
        cost2=10**9
        for j in range(i):
            if A[j]<A[i]:
                cost1=min(cost1,B[j])
        
        for k in range(i+1,n):
            if A[k]>A[i]:
                cost2=min(cost2,B[k])
        
        if (cost1 != 10**9 and cost2 != 10**9):
            cost3 = min(cost3, B[i] +cost1 + cost2)
 
    # No such triplet found
    if (cost3 == 10**9):
        return -1
    return cost3
            