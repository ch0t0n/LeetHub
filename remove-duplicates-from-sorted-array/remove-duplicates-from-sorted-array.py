class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n-1):
            if nums[i]!='d':
                for j in range(i+1,n):
                    if nums[i] == nums[j]:
                        nums[j] = 'd'
        
        d = nums.count('d')
        k = n-d
        
        for j in range(d):
            nums.remove('d')
        
        
        return k