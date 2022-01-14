# Check reverse of number and number are equal
# Input one integer

def main(n): # Logic to Reverse the No 
    ans=0
    while(n>0):
        rem=n%10
        ans=(ans * 10) + rem
        n=n//10
    return ans

if __name__ == '__main__':
    no1=int(input())
    if main(no1)==no1:
        print("Yes")
    else:
        print("No")