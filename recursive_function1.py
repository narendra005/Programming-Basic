# recursive functions
# input 1 positive number
def main(N):
    if N==0: 
        return
    else:
        print(N,end=" ")
        main(N-1)
if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(200000)
    main()
    N=int(input())
    main(N)