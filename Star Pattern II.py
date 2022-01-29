#Write a program to input an integer N from user and print hollow inverted right triangle star pattern of N lines using '*'.
#See example for clarifications.

def main(rows):
    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            if i == 1 or i == rows or j == 1 or j == i:
                print('*', end = '')
            else:
                print(' ', end = '')
        print()

if __name__ == '__main__':
    rows=int(input())
    main(rows)