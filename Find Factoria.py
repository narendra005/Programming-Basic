#Write a program to find the factorial of the given number A.
#  Factorial of 4 = 4 * 3 * 2 * 1 = 24
def fact(A):
    if A<=1:
        return 1
    return A * self.solve(A-1)
class Solution:
    def solve(self, A):
        if A==0 : return 1
        return A * self.solve(A-1)	