#Given a string A of size N, find and return the longest palindromic substring in A.
#Substring of string A is A[i...j] where 0 <= i <= j < len(A)
#Palindrome string:
#A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
#Incase of conflict, return the substring which occurs first ( with the least starting index).

def longestPalindrome( A):
	m = ''  # Memory to remember a palindrome
	n=len(A)
	for i in range(n):  # i = start, O = n
		for j in range(n, i, -1):  # j = end, O = n^2
			if len(m) >= j-i:  # To reduce time
				break
			elif A[i:j] == A[i:j][::-1]:
				m = A[i:j]
				break
	return m