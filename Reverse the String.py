#Given a string A of size N.
#Return the string A after reversing the string word by word.
#Input 1: A = "the sky is blue"
#Input 2: A = "this is ib"  
#output 1:"blue is sky the"
Output 2:"ib is this"    

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        
        def Reverse_string(A):
            return A[::-1]
    
        if A[-1]==" " :
            A1=A[::-1]
            A1=A1[1::]
        else:
            A1=A[::-1]
        start=0
        ans=[]
        for i in range(len(A1)):
            if A1[i]==" ":
                ans.append(Reverse_string(A1[start:i]))
                #print(Reverse_string(A1[start:i]),end=" ")
                start=i+1
        
        if A1[start]!=None:
            ans.append(Reverse_string(A1[start:len(A1)]))
        
        return " ".join(ans)