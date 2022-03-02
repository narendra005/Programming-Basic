#The Fibonacci numbers are the numbers in the following integer sequence.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:
#Fn = Fn-1 + Fn-2
#Given a number A, find and return the Ath Fibonacci Number.
#Given that F0 = 0 and F1 = 1.
#write a recursive function for this 

class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A==1 : return 1
        if A<=0 : return 0
        return self.findAthFibonacci(A-1) + self.findAthFibonacci(A-2)    