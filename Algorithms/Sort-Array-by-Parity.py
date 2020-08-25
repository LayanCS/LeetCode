# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.
 
# Example 1:
# Input: [3,1,2,4], Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        '''
        :type A: List[int]
        :rtype: List[int]
        '''
        # one line solution using lambda:
        # return sorted(A, key= lambda x: x%2 )
       
        start = 0
        end = len(A) -1
        while start < end: 
            if A[start]%2 == 0:# keep the even at where it is
                start +=1
            else:
                A[start], A[end] = A[end], A[start] # swap the odd number to the back
                end -=1

        return A
