#Given two binary strings, return their sum (also a binary string).
#Example: a = "100"  b = "11"
#Return a + b = "111" Try Adding the Numbers as binary rather converting to decimal and add 

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):        
        n1=len(A)
        n2=len(B)
        n=0
        if n1>n2:
            B=B.zfill(n1)
            n=n1
        elif n2>n1:
            A=A.zfill(n2)
            n=n2

        carry=0
        ans=[]
        n=len(A)
        carry=0
        ans=[]
        for i in range(n-1,-1,-1):
            a=int(A[i])
            b=int(B[i])
            
            if a&b==1 and carry==1:
                ans.append(1)
            elif a&b==1 and carry==0:
                ans.append(0)
                carry=1
            elif a|b==1 and carry==1:
                ans.append(0)
                carry=1
            elif a|b==1 and carry==0:
                ans.append(1)
            elif a|b==0 and carry==1:
                ans.append(1)
                carry=0
            elif a|b==0 and carry==0:
                ans.append(0)
        
        if carry==1:
            ans.extend([1,0])
        str1=''
        ans=ans[::-1]
        for i in ans:
            str1+=str(i)
        #print(str1,Binary_Decimal(int(str1)))A
        str1=int(str1)
        return str1
