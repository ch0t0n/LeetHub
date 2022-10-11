class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negs = []
        n = len(nums)
        pos = []
        for i in range(n):
            if nums[i] < 0:
                negs.append(nums[i])
            else:
                pos = nums[i:]
                break
        
        i, j = len(negs)-1, 0
        squared = []
        while i>=0 and j<len(pos):
            a, b = negs[i]**2, pos[j]**2
            if a < b:
                squared.append(a)
                i -= 1
            else:
                squared.append(b)
                j += 1
        while i>=0:
            a = negs[i]**2
            squared.append(a)
            i -= 1
        while j<len(pos):
            b = pos[j]**2
            squared.append(b)
            j += 1
        return squared
                