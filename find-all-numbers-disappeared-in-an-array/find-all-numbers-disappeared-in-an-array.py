class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        setn = set(nums)
        dis = []
        for i in range(n):
            if i+1 not in setn:
                dis.append(i+1)
        
        
        return dis
                
                