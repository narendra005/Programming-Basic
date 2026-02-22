# Print 1..N Using Recurisive Function
# Input is single digit positive numbers
# 
def main(N):
    j=N
    if N==0:
        print(end="")
        return 1
    else:
        main(N-1)
        print(N,end=" ")      
if __name__ == '__main__':
    N=int(input())
    main(N)
    print("End")