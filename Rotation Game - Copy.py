#You are given a constant array A.
#You are required to return another array which is the reversed form of input array.
#Input A = [1,2,3,4,5]
# B = 3 Which means no rotation
# output is 3,4,5,1,2 
# After each rotation the right most digit becomes first and so on for 1 rotation it would 5 1 2 3 4 second  4 5 1 2 3 and so on 
# Inputs 

def main(a,k):
    ans=[]
    n=len(a)
    # If rotation is greater
    # than size of array
    k = k % n;
 
    for i in range(0, n):
 
        if(i < k):
 
            # Printing rightmost
            # kth elements
            #print(i,a[n + i - k], end = " ");
            ans.append(a[n + i - k])
 
        else:
 
            # Prints array after
            # 'k' elements
           # print(i,a[i - k], end = " ");
            ans.append(a[i - k])
    return ans

if __name__ == '__main__':
    A=[int(i) for i in input().split()]
    B=int(input())
    A.pop(0) # Here 5 1 2 3 4 5 given as input where first 5 is number of element so just removing it from list
    L=main(A,B)
    for i in L:
        print(i,end=" ")
  