# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle. 
# Note that the row index starts from 0.
# Input: 3 , Output: [1,3,3,1]

# import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        :type rowIndex: int
        :rtype: List[int]
        '''
        
        if rowIndex > 33: return None
        
        # total = 2**rowIndex # the sum of the nth row is 2^row-number
        # length = (rowIndex + 1)
        
        if ((rowIndex + 1) % 2) != 0:
            midPoint = floor((rowIndex + 1)/2) # the non-symmetric number
        else:
            midPoint = -1
        
        output = [0] * (rowIndex + 1)
        i = 0
        
        while i < ceil((rowIndex + 1)/2):
            if i == midPoint:
                output[i] = int(factorial(rowIndex) / (factorial(i) * factorial(rowIndex-i)))
            else:
                output[i] = int(factorial(rowIndex) / (factorial(i) * factorial(rowIndex-i)))
                output[rowIndex-i] = output[i]
            i = i+1
                
        return output
