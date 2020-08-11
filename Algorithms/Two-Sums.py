# Two Sum - Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        # one-pass approach
        seen = {} # dictionary
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining not in seen:
                seen[nums[i]] = i
            else:
                return [seen[remaining], i]
        return []

        
        # initial solution
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i: break
        #         if nums[i] + nums[j] == target: return [j, i]
