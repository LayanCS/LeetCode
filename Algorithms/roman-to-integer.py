# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Input: "MCMXCIV", Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        :type s: str
        :rtype: int
        '''
 
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        total, temp = 0, 0 # total, previous roman numeral
        
        for value in s[::-1]: # calculating in reverse will reduce overhead 
            if roman[value] >= temp:
                total += roman[value]
            else:
                total -= roman[value]
            temp = roman[value]
            
        return total
