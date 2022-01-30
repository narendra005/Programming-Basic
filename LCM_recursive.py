def addBinary(A, B):
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
    for i in range(n-1,-1,-1):
        a=int(A[i])
        b=int(B[i])
        if i==0 and carry==1:
            ans.extend([1,0])
        elif a&b==1 and carry==1:
            ans.append(1)
        elif a&b==1 and carry==0:
            ans.append(0)
            carry=1
        elif a|b==1 and carry==1:
            ans.append(0)
        elif a|b==1 and carry==0:
            ans.append(1)
        elif a|b==0 and carry==1:
            ans.append(1)
        elif a|b==0 and carry==0:
            ans.append(0)
        print(i,ans,carry)
    str1=''
    for i in ans:
        str1+=str(i)
    return str1
A = "1110000000010110111010100100111"
B = "0000000000010110111000000101001"
print(addBinary(A,B))