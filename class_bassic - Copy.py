import math
class Temperature:
    def __init__(self,temp):
        self.temp=temp
       
    def convertcelsius(self):
        ans=(self.temp - 32) * .5556
        if ans>0 and len(str(ans))>5:
            ans=str(ans)
            r=ans.find(".",0)
            ans=ans[0:r+3]   
        return str(ans) + " degree celsius"
    def convertfahrenheit(self):
        ans=(self.temp * 1.8) + 32
        print(ans)
        if ans>0 and len(str(ans))>5:
            ans=str(ans)
            r=ans.find(".",0)
            ans=ans[0:r+3] 
            if ans[-1]=='0':
                ans=ans[0:len(ans)-1]
        return str(ans) + " degree fahrenheit"
    
    
def tempconversion(t):
    temp=Temperature(t)
    print(temp.convertcelsius())
    print(temp.convertfahrenheit())
tempconversion(99)