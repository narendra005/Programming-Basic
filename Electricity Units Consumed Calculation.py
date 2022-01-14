#Calculate Electricity of Consumer in Following format
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
# Simple calculation of Bills based upon no of units consumed.
# Input is positive integer
def main(units):
    total_bill=0
    if units<=50:
        total_bill=units*.5
    elif units<=150:
        total_bill=50*.5+(units -50)*.75
    elif units<=250:
        total_bill=50*.5+100*.75+(units -150)*1.2
    else :
        total_bill=50*.5+100*.75+100*1.2+(units -250)*1.5
## multiply for Surcharge
    return int(total_bill*1.2)

if __name__ == '__main__':
    units=int(input())
    print(main(units))