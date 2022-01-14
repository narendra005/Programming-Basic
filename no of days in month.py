# Given a month number, A and an year, B, return the number of days in that month (take leap years into account).
#First argument is an integer A denoting the month number.Second argument is an intege B denoting the year.
#1. Input A = 2 , B = 2020
#1. output 29
class Solution:
    def leap_year(self,year):
        if year%100==0 & year%400==0:
            return True
        elif year%4==0:
            return True
        else: 
            return False
    def solve(self, A, B):
        month=0
        if A in (1,3,5,7,8,10,12):
            month=31
        elif A in (4,6,9,11):
            month=30
        else:
            if leap_year(self,year):
                month=29
            else:
                month=29
        return month