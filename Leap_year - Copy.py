# Given a Year and Month Find if the the Year is Leap year or not
#
class Solution:
    def solve(self, A, B):
        month=0
        if A in (1,3,5,7,8,10,12):
            month=31
        elif A in (4,6,9,11):
            month=30
        else:
            if  A%400==0:
                month=29
            elif A%100==0:
                month=28
            elif A%4==0:
                month=29
            else:
                month=28
        return month