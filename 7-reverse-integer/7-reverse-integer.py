class Solution:
    def reverse(self, x: int) -> int:        
        n = str(x)
        n2 = ''
        if (n[0]!='-'):
            for i in range(len(n)-1,-1,-1):
                n2 = n2+(n[i])
        elif (n[0]=='-'):
            n2 = n2+n[0]
            for i in range(len(n)-1,0,-1):
                n2 = n2+n[i]
        n3 = int(n2)
        if (n3<2147483648 and n3>-2147483648): return n3
        else: return 0