class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        while (x > 0):
            remainder = x % 10
            reverse = (reverse*10) + remainder
            x = x // 10
            
        if temp == reverse:
            return True
        else:
            return False