#Find Max of the three integers given as input
#contraints input of numbers only 
# Input in 1 single line of seperated by space.
def main(A,B,C):
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    if (A>=B)&(A>=C):
        return A
    elif (B>=A)&(B>=C):
        return B
    elif (C>=A)&(C>=B):
        return C
    elif(A==B)&(A==C):
        return A
if __name__ == '__main__':
    A,B,C=(int(i) for i in input().split())
    print(main(A,B,C))