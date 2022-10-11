class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sets = set(nums)
        dis = []
        for i in range(n):
            if i+1 not in sets:
                dis.append(i+1)
        
        return dis
        