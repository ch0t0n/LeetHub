class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        res = []

        while i < m and j < n:
            ai , bj = nums1[i], nums2[j]
            if ai < bj:
                res.append(ai)
                i += 1
            else:
                res.append(bj)
                j += 1

        while i < m:
            ai = nums1[i]
            res.append(ai)
            i += 1

        while j < n:
            bj = nums2[j]
            res.append(bj)
            j += 1
        
        for i in range(m+n):
            nums1[i] = res[i]
        