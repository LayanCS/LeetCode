# Reverse Integer - Given a 32-bit signed integer, reverse digits of an integer.
# Input: 123 Output: 321
# Input: -123 Output: -321

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            s = str(x)
            if x >= 0: # positive
                reverse = int(s[::-1])
            else:
                reverse = -int(str(abs(x))[::-1])
        if reverse >= 2**31-1 or reverse <= -2**31:
            return 0
        else: 
            return reverse
            
# You can use also use: Reverse.bit_length() < 32
