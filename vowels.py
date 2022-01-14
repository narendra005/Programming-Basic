# You are given a lowercase latin alphabetic character C. You have to tell whether it is a vowel or not.The characters 'a', 'e', 'i', 'o', and 'u' are called vowels.
# input is one character.
def main(char1):
    if char1 in ('a','e','i','o','u'):
        return 1
    else: 
        return 0

if __name__ == '__main__':
    char1=input()
    print(main(char1))