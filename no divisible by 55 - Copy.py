#Take input of Number and check if its divisible by 5 and 11 return 1 if yes else 0
# Simple assumption no has to be divisible by 55 
def main(A):
    return(1 if A%55==0 else 0)
if __name__ == '__main__':
    A=int(input())
    print(main(A))