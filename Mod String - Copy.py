#You are given a huge number in the form of a string A where each character denotes a digit of the number.
#You are also given a number B. You have to find out the value of A % B and return it.
#Return a single integer denoting the value of A % B.
class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def findMod(self, A, B):
        cnt=1
        ans=0
        for i in range(len(A)-1,-1,-1):
            ans=ans+(int(A[i])*cnt )%B
            cnt=(cnt*10)%B
        return ans%B