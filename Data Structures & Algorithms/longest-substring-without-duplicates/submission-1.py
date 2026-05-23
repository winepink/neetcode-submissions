class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l=0
        cnt=0
        ans=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            while(count[s[r]]>1):
                count[s[l]] -= 1
                l += 1                
            ans = max(ans, r - l + 1)
        return ans