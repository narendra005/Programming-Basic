# Subarray with digit Sum ==0 
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1 else return 0.

def sub_array(A):
    sum1=0
    set1=set()
    for i in range(len(A)):
        sum1+=A[i]
        
        if sum1==0 or sum1 in set1:
            return 1
        set1.add(sum1)
    return 0