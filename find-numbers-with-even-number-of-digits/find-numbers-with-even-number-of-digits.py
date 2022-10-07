class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        digits = 0

        for num in nums:
            while num >= 1:
                num = num / 10
                digits += 1
            if digits % 2 == 0:
                count += 1
            digits=0
        
        return count