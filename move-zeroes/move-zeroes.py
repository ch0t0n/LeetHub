class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
            nums.append(0)
        