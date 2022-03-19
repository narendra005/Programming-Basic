# Spiral Matrix 
# if n is 2 then print sprial matrix till 4
# 1 2 
# 4 3

def main(n):
    matrix = [[None]*n for _ in range(n)]
    row=left=0
    bot=right=n-1
    count=1
    dir=0 # 0 is left to right , 1 is for right to left
    while row<=bot and left<=right: 
        if dir==0:
            for col in range(left,n):
                matrix[row][col] = count
                count+=1
        
        elif dir==1:
            for col in range(right,-1,-1):
                matrix[row][col]=count
                count+=1
                
        row+=1
        dir+=1
        dir=dir%2
    return matrix
if __name__ == '__main__':
    A=int(input())
    ans=main(A)
    row=0
    for i in ans:
        for j in range(len(i)):
            print(ans[row][j],end=" ")
        row+=1
        print()