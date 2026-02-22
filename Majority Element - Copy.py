#Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
#You may assume that the array is non-empty and the majority element always exist in the array.
#	Input : [2, 1, 2]
#Return  : 2 which occurs 2 times which is greater than 3/2.
## Apporach for Every element we are making pair if the pair has same element move else we make the number as majority 
# This assumes all element present more n /2 times will have 1 or more numbers after pairing all the digits 
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        max1=A[0]
        count1=1

        for i in range(1,len(A)):
            if A[i]==max1:
                count1+=1
            
            elif count1==0:
                max1=A[i]
                count1=1
                
            else:
                count1-=1

        count1=0
        for i in A:
            if i==max1:
                count1+=1
        
        if count1>len(A)//2:
            return max1