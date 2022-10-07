class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        even_arr = [x for x in arr if x%2==0]
        if 0 in arr:
            arr.remove(0)
        
        for v in even_arr:            
            if v/2 in arr:
                return True
        
        return False
        