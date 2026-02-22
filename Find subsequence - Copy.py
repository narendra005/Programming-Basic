#Given two strings A and B, find if A is a subsequence of B.
#Return "YES" if A is a subsequence of B, else return "NO".
#The first argument given is the string A.
#The second argument given is the string B.
#Input  1:#    A = "bit" #    B = "dfbkjijgbbiihbmmt"
#Output 1:#    YES
#Input  2:#    A = "apple"     B = "appel"
#Output 2:#   "NO"

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        ans=[]
        temp1=0
        if A in B:
            return "YES"
        elif len(A)>len(B):
            return "NO"
        for i in range(len(A)):
            a=A[i]
            if A[i] in B:
                temp1=B.find(A[i],temp1)
                ans.append(temp1)
        
        for i in range(1,len(ans)):
            if ans[i]<ans[i-1]:
                return "NO"
        return "YES"