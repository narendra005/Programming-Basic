#Problem Description Reverse the bits of an 32 bit unsigned integer A.
# Need to reverse the Number and add 32-number of digits to it 

def reverseBits(n) :   
    rev = 0
    cnt=0
    while (n > 0) :
         
        # bitwise left shift 'rev' by 1
        rev = rev << 1 ##    
        # if current bit is '1'
        if (n & 1 == 1) :
            rev = rev ^ 1
         
        # bitwise right shift 'n' by 1
        n = n >> 1 ## same n=n//2
        cnt+=1 
     
    # required number
    
    return rev,cnt

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ## The logic of while is written to get the no of digits in number
        ## all numbers 2**k<=N for K is number of digits in 
        N1,count1=reverseBits(A)

        return N1<<(32-count1)