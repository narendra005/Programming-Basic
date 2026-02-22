#Problem Description
#Given a number A, we need to find sum of its digits using recursion.
def solve(self, A):
        def sum_rec(A):
            if A==0:
                return 0
            return A%10 + sum_rec(A//10)
        return sum_rec(A)