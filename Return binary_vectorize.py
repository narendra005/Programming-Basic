#Given a Numpy array of integers as input to the function, complete the given function that converts each element in the array into its binary representation.
#For example: In binary, 5 = 101, 7= 111, 10= 1010.
#Note: You are not allowed to use the inbuilt bin() function and Both input and output array are of datatype 'int'.

import numpy as np
def binary(arr):
    def BinaryToDecimal(n):
        ans=0
        p=1
        while(n>0):
            rem=n%2
            ans=ans+rem*p
            p=p*10
            n=n//2
        return ans

    vec= np.vectorize(BinaryToDecimal)
    return vec(arr)