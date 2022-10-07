class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mx1 = max(nums)
        nums = [x for x in nums if x!=mx1]
        if nums:
            mx2 = max(nums)
        else:
            return mx1
        nums = [x for x in nums if x!=mx2]
        if nums:
            mx3 = max(nums)
        else:
            return mx1
        
        return mx3
    