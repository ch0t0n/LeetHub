class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cm = ""
        j = 0
        n = len(strs)
        m = len(strs[0])
        for i in range(m):
            for j in range(n-1):                
                if (i>=len(strs[j])) or (i>=len(strs[j+1])):
                    return cm
                if (strs[j][i] != strs[j+1][i]):
                    return cm
            cm = cm + strs[0][i]
        return cm        
            
                
        
        
        