#There are 100 doors, all closed. In a nearby cage are 100 monkeys.
#The first monkey is let out, and runs along the doors opening every one. The second monkey is then let out, and runs along the doors closing the 2nd, 4th, 6th,… - all the even-numbered doors. The third monkey is let out. He attends only to the 3rd, 6th, 9th,… doors (every third door, in other words), closing any that is open and opening any that is closed, and so on. 
#After all 100 monkeys have done their work in this way, what state are the doors in after the last pass?
# Logic 
#1. if N is Power of 2 then 1
#2. Reach to 2 power which is lower than N which we say ans
#3. ( N -ans )*2 +1
## Here N & N-1==0 for all power of 2 
def last_manstanding(N):
    if N&(N-1)==0: return 1
    else:
        i=2
        while(i<N):
            i=i*2
        i=i//2
    return (N - i)*2+1