class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        neg = 0
        ar1, ar2 = [], []
        for v in nums:
            if v < 0:
                neg += 1
                ar1.insert(0, v**2)
            else:
                break

        for v2 in range(neg, n):
            val = nums[v2]
            ar2.append(val**2)

        i, j = 0, 0
        sorted_list = []

        while i < len(ar1) and j < len(ar2):
            a, b = ar1[i], ar2[j]
            if a < b:
                sorted_list.append(a)
                i += 1
            else:
                sorted_list.append(b)
                j += 1

        while i < len(ar1):
            sorted_list.append(ar1[i])
            i += 1

        while j < len(ar2):
            sorted_list.append(ar2[j])
            j += 1
        
        return sorted_list