# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Input: "abccccdd" , Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        :type s: str
        :rtype: int
        '''
        # evey letter in a palindrome words occures an even number of time except one 

        evens = sum(v & ~1 for v in Counter(s).values())
        return evens + (evens < len(s))
    
# Example with Counter({'b': 3, 'a': 2, 'c': 2})
# it will sum it as if it was {'b': 2, 'a': 2, 'c': 2} (all even values)
# then checks if the sum < len(s) in this case --> 8 < true (1)
