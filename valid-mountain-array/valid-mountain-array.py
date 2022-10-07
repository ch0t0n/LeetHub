class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n<3:
            return False
        
        mid = 0
        if arr[0] >= arr[1]:
            return False
        for i in range(1,n-1,1):
            if arr[i+1] == arr[i]:
                return False
            if arr[i+1] < arr[i]:
                mid = i
                break
        
        if mid == 0:
            return False
        
        
        for j in range(mid,n-1,1):
            if arr[j+1] >= arr[j]:
                return False
        
        return True
            
        