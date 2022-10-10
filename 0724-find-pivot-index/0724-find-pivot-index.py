class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        n = len(nums)
        ls, rs = 0, 0
        for i in range(n):
            if i==0:
                ls = 0
                rs = sum(nums[i+1:])                
            elif i==n-1:
                ls = sum(nums[:i])
                rs = 0
            else:
                ls = sum(nums[:i])
                rs = sum(nums[i+1:])
            if ls == rs:
                return i
        return -1
            
                
            
        
        