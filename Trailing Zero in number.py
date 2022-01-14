# Trailing Zero in number
# 
class Solution:
    def trailingZeroes(self, A):
        product=1
        count=0
        if A==0:
            return 0
        else:
            for i in range(1,A+1):
                product=product*i
            while(product>0):
                if product%10==0:
                    count=count+1
                else:
                    break
                i=i-1
                product=product//10
        return count