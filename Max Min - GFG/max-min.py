class Solution:
    def findSum(self,A,N): 
        #code here
        minv, maxv = A[0], A[0]
        for v in A:
            if v < minv:
                minv = v
            if v > maxv:
                maxv = v
        
        return minv+maxv



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends