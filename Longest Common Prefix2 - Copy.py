#Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.
#Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
#For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".


def longestCommonPrefix(A):
    if len(A)==1:
        return ''.join(A)

    min1=len(A[0])
    for i in range(len(A)):
        min1=min(min1,len(A[i]))
    
    for i in range(1,len(A)):
        ans=[]
        str1=A[i-1]
        str2=A[i]
        for k in range(min1):
            if str1[k]==str2[k]:
                ans.append(str1[k])

    if len(ans)==0:
        return ""
    else:
        return ''.join(ans)