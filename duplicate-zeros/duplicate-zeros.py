class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        result = []

        for v in arr:
            if v == 0:
                result.append(v)
                result.append(v)
            else:
                result.append(v)

        for i in range(n):
            arr[i] = result[i]