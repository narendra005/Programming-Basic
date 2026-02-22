#Print table of Given Numbers
# input is integer.
def main(N):
    for i in range(1,11,1):
        print(N, "*" ,i,"=",N*i)
    return 0

if __name__ == '__main__':
    N=int(input())
    main(N)