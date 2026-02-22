#Write a recursive function that checks whether a string A is a palindrome or Not.
#Return 1 if the string A is palindrome, else return 0.
#Note: A palindrome is a string that's the same when reads forwards and backwards.

def solve(A):
    n=end=len(A)
    start=-1
    def palindrome(A,start,end):
        if start>end:
            if len(A)%2==0: return 1
            else :   return 0
        elif start==end:
            return 1
        if A[start]!=A[end]:
            #print(start,A[start],A[end])
            return 0
        #print(start,end,A[start],A[end])
        return palindrome(A,start+1,end-1)
    return palindrome(A,start+1,end-1)