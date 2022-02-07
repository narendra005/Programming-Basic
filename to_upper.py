#You are given a function to_upper() consisting of a character array A.
#Convert each charater of A into Uppercase character if it exists. If the Uppercase of a character does not exist, it remains unmodified.
#The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.
#Return the uppercase version of the given character array.
def to_upper(A):
	for ch in range(len(A)):
		a=ord(A[ch])
		if a>96 and a<123:
			A[ch]=chr(a-32)
	return A