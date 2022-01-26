# Find the Sume of max subarray 
# Subarray can have positive or negative values

def maxSubArraySum(A):
    size=len(A)
    max_so_far = - 1
    max_ending_here = 0
    temp1=max(A)
    
    if temp1<0:
        return temp1
    elif n==1:
        return A[0]
    
    for i in range(0, size):
        max_ending_here = max_ending_here + A[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
        
    return max_so_far