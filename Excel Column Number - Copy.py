#Given a column title as appears in an Excel sheet, return its corresponding column number.
#  ABCD output =19010


class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
        result = 0;
        for ch in range(len(A)):
            result *= 26;
            result =result + (ord(A[ch]) - ord('A') + 1); ## Gives the Character position 
        return result;