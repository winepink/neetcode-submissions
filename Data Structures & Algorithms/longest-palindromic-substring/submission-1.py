class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            # loop stopped after going one step too far
            return s[l + 1:r]

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(ans):
                ans = odd

            if len(even) > len(ans):
                ans = even

        return ans