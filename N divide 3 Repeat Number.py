#You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
#If so, return the integer. If not, return -1.
#If there are multiple solutions, return any one.
#Input: [1 2 3 1 1]
#Output: 1 
#1 occurs 3 times which is more than 5/3 times.
# Here we are creating dictionary for number of occurance 
# Scanning through dictionary as the problem say first element .


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        D={}
        n=len(A)//3
        for i in range(len(A)):
            a=A[i]
            if a not in D:
                D[a]=1
            else:
                D[a]+=1

        for i in range(len(A)):
            a=A[i]
            if D[a]>n:
                return a
        else : return -1
            
                
        

