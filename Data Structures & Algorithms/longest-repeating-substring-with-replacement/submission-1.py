class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l=0
        maxFreqinWin=0
        ans=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxFreqinWin=max(maxFreqinWin,count[s[r]])
            while(r-l+1)-maxFreqinWin>k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        return ans
