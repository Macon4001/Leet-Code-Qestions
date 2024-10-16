class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # If the number is negative or if it ends with 0 (but is not 0 itself), it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Reverse the second half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Check if the first half is equal to the reversed second half
        # For odd-length numbers, we can get rid of the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
