class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 1
        l, r = 0, 1
        while r < len(s):
            while s[r] in s[l: r]:
                l += 1
            r += 1
            maxLength = max(maxLength, r - l)   
        return maxLength