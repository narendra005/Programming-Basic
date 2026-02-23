
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121 # Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:  # Input: x = -121 # Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3: # Input: x = 10 # Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
class Solution:
    def reverse_number(self, n: int):
        rev = 0
        # Handle negative numbers if needed, 
        # but for Palindrome problems, negatives are usually False
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n = n // 10
        return rev

    def isPalindrome(self, x: int) -> bool:
        # Step 1: Handle edge cases (Negative numbers aren't palindromes)
        if x < 0:
            return False
            
        # Step 2: Compare the original x with its reverse
        # Fixed: Changed 'i' to 'x'
        return x == self.reverse_number(x)