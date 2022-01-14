## Beggers outside temple
#There are N (N > 0) beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to his faith and ability) to some K beggars sitting next to each other.
#Given the amount donated by each devotee to the beggars ranging from i to j index, where 1 <= i <= j <= N, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
#Example:
#Input:
#N = 5, D = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
#Return: [10, 55, 45, 25, 25]

def beggers(N, D):
    Beggers=[0] * N
    for devotee in D:
        start,end,coins=devotee
        start-=1
        end-=1
        for i in range(start,end+1):
            Beggers[i]+=coins
    return Beggers