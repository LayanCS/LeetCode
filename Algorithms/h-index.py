# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# Input: citations = [3,0,6,1,5], Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#             received 3, 0, 6, 1, 5 citations respectively. 
#             Since the researcher has 3 papers with at least 3 citations each and the remaining 
#             two with no more than 3 citations each, her h-index is 3.
import numpy as np

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        :type citation: List[int]
        :rtype: int
        '''
        # empty or zero or negative list
        if not citations or not np.any(citations) or max(citations) < 0 : return 0
        
        citations = sorted(citations, reverse = True)
        for i, v in enumerate(citations):
            if v >= i+1:
                h_index = i+1
            else:
                return h_index
        return i+1
