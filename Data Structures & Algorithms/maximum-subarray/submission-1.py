class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax=nums[0]
        ans=nums[0]
        for x in nums[1:]:
            curMax=max(x,x+curMax)
            ans=max(ans,curMax) 
        return ans