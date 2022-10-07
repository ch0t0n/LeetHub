class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1):
            if nums[i]%2==1:
                for j in range(i+1,n):
                    if nums[j]%2==0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
        return nums