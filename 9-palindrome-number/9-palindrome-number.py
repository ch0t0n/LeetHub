class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        n2 = ''
        for i in range(len(n)-1,-1,-1):
            n2 = n2+n[i]
        if (n2==n): return True
        else: return False