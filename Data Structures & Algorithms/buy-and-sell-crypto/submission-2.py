class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar=float("inf")
        diff=0
        for price in prices:
            if price< minsofar:
                minsofar=price
            diff=max(diff,price-minsofar)
        return diff