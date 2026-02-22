#Write a program to input an integer N from user and print hollow diamond star pattern series of N lines.
# Input is single integer for pattern
# See example for clarifications over the pattern.
#Belo output is for input 4 
#********
#***  ***
#**    **
#*      *
#*      *
#**    **
#***  ***
#********
def main(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        
        for j in range((n-i)*2):
            print(" ",end="")
        
        for j in range(i,0,-1):
            print("*",end="")

        print()
        
## Loop 2 starts
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        
        for j in range((n-i-1)*2):
            print(" ",end="")
        
        for j in range(i+1):
            print("*",end="")
        print()

if __name__ == '__main__':
    N=int(input())
    main(N)