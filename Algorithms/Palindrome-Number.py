# Palindrome Number - Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Input: 121 Output: true
# Input: -121 Output: false


class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        :type x: int
        :rtype: boolean
        '''
        # without converting to string
        if x < 0: #if negative
            return False
        temp = x
        y = 0
        while(temp>0):
            remainder = temp % 10
            y = (y * 10) + remainder
            temp = temp // 10
        
        if x == y:
            return True
        else:
            return False
            
# with string
# return False if x < 0 else str(x) == str(x)[::-1]
