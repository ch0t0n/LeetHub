class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
                for j in range(1,n,1):
                    if (j!=i):
                        if ((nums[i]+nums[j])==target):
                            ans.append(i)
                            ans.append(j)
                            return ans
                        