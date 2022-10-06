class Solution(object):
    def sortedSquares(self, nums):
        for i,v in enumerate(nums):
            nums[i] = v**2

        nums = sorted(nums)
        
        return nums