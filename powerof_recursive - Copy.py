# Find the a **b using recursive function
# Input is no1 and its power b
# input two should be positive
def main(N,power):
    if power==0:
        return 1
    else:
        ans= N * main(N,power -1)
        return ans

if __name__ == '__main__':
    N=int(input())
    power=int(input())
    print(main(N,power))