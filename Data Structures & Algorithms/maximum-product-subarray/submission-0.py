class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            if x < 0:
                curMax, curMin = curMin, curMax

            curMax = max(x, curMax * x)
            curMin = min(x, curMin * x)

            ans = max(ans, curMax)

        return ans