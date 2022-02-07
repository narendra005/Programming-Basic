#Find number of occurrences of bob in the string A consisting of lowercase english alphabets.
# Input "bobob" output 2

def solve(A):
    ans=temp1=0
    j=0
    while(temp1!=-1):
        temp1=A.find('bob',j)
        if temp1!=-1:
            ans+=1
            j=temp1+1
        print(temp1,j,ans)
    return ans