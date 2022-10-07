class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        if n == 1:
            return [-1]

        for i in range(n-1):
            max_val = max(arr[i+1:])
            arr[i] = max_val

        arr[-1] = -1
        
        return arr