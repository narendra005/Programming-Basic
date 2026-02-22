## Find the Good Pair a good pair is subarray if len is even and greater than B and if len is odd then sum is less than odd
def solve(A, B):
    for i in range(1, len(A)):
        A[i] = A[i-1]+A[i]

    count = 0 
    for i in range(len(A)):
        for j in range(i, len(A)):
            if i == 0:
                arraySum = A[j]
            else:
                arraySum = A[j]-A[i-1]

            if arraySum < B and (j+1-i)%2 == 0:
                count += 1
            elif arraySum > B and (j+1-i)%2 != 0:
                count += 1
            print(A[i],A[j],arraySum)
    return count