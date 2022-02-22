# Write a recursive function that, given a string S, prints the characters of S in reverse order.
# Using Recursioon Hello would become : olleh

def main(A,end):
    if end<=0:
        print(A[end])
        return 
    else:
        print(A[end],end="")  
    return main(A,end-1)

if __name__ == '__main__':
    A=input()
    n=end=len(A)
    main(A,end-1)