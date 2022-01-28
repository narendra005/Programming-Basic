#Richard Hendricks, a mastermind on compression algorithms, in an employee of Hooli in the Silicon Valley.
#One day, he finally decided to quit and work on his new idea of middle - out algorithm.

#He needed to work at the bit - level to compress data. He, eventually, encountered this problem.
#There was an array A of N integers. He had to perform certain operations on the elements.
#In any one operation, two indices i and j (i < j) are chosen, and A[i] is replaced with A[i] & A[j],
#and A[j] is replaced with A[i] | A[j], where & represents the Bitwise AND operation and | represents the Bitwise OR operation.
#This operation is performed over all the pairs of integers in the array.
#Help Richard find the Bitwise XOR of all the elements after performing the operations.
#Return a single integer denoting the XOR of the elements after performing the operations.
#A = [1, 3, 5]
#After performing the operations, the array becomes [1, 1, 7].
#The XOR of all the elements of this array is 7.
#There can be other arrays too but we can prove that the XOR will always be 7.

class Solution:
    # @param A : list of integers
    # @return an integer
    def compressBits(self, A):
        for i in range(len(A)-1):
            temp=A[i]&A[i+1]
            temp1=A[i]|A[i+1]
            A[i]=temp
            A[i+1]=temp1    
            xor=0
            for i in A:
                xor=xor^i
            return xor

