#In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographicaly in this alien language else return 0.
# First argument is a string array A of size N. Second argument is a string B of size 26 denoting the order.
# Input  A = ["hello", "scaler", "interviewbit"] # B = "adhbcfegskjlponmirqtxwuvzy"
# Output The order shown in string B is: h < s < i for the given words. So return 1.
# Input  A = ["fine", "none", "no"] B = "qwertyuiopasdfghjklzxcvbnm"
# Output  "none" should be present after "no". Return 0.
def solve(A, B):
    n=len(A)
    B1={}
    # Creation of Diction for New Alphabet
    for i in range(len(B)):
        B1[B[i]]=i+1

    for i in range(1,len(A)):
        lower=A[i-1]
        upper=A[i]
        upper_len=len(upper)
        lower_len=len(lower)
        j=0
        while(lower_len>0 and upper_len>0):
            print(j,lower,upper,B1[lower[j]],B1[upper[j]])
            if B1[lower[j]]<B1[upper[j]]:
                upper_len=1
            
            elif B1[lower[j]]==B1[upper[j]]:
                if len(lower)>len(upper):
                    upper_len=1
                else:
                    pass
                           
            else:
                return 0  
            upper_len-=1
            lower_len-=1
            j+=1
    return 1