# HCF of Number using recurisve fuction
import sys
sys.setrecursionlimit(150000)
def HCF_NU(A,B):
    if A==0:
        return B
    else:
        return HCF_NU(B%A,A)