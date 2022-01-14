#Write a program to input from user five numbers(A, B, C, D & E) representing marks of student in 5 subjects out of 100. You have to calculate percentage and then Grade of each student.
#If percentage >= 90% : Grade A
#. If percentage >= 80% : Grade B
#. If percentage >= 70% : Grade C
#. If percentage >= 60% : Grade D
#. If percentage >= 40% : Grade E. 
#. If percentage < 40% : Grade F

def main(per):
    if per>=90:
        return (str(per)+' A')
    elif per>=80:
        return (str(per)+' B')
    elif per>=70:
        return (str(per)+' C')
    elif per>=60:
        return (str(per)+' D')
    elif per>=40:
        return (str(per)+' E')
    else:
        return (str(per)+' F')

if __name__ == '__main__':
    N=list(input().split())
    sum1=sum(int(i) for i in N)
    per=sum1//5
    print(main(per))