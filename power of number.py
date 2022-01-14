# Power of number A **B 
# Inpput is 2 Numbers 
def main(N,power):
    out=1
    if power==0:
        return 1 
    else :
        while(power>0):
           # print(out,power)
            out= out * N 
            power=power-1   
        return out

if __name__ == '__main__':
    N=int(input())
    power=int(input())
    print(main(N,power))