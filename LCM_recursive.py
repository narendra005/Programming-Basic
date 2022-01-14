# LCM of Number 
# LCM * HCF = A * B 
def find_HCF(A,B):
    if A==0:
        return B
    else:
        return int(find_HCF(B%A,A))

def LCM_2(A,B):
    return A*B/(find_HCF(A,B))