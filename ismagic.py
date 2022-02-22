#Given a number A, check if it is a magic number or not.
#A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. 
#If the single digit comes out to be 1, then the number is a magic number.
# A = 83557 output 1

def solve(A):
    def magic_no(A):
        if A==0:
            return 0
        return A%10 + magic_no(A//10)
    ans=magic_no(83557)
    while ans>9:
        ans=magic_no(ans)
    if ans==1 :return 1
    else: return 0