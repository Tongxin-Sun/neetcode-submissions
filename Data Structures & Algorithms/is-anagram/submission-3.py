class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1, c2 = [0] * 26, [0] * 26
        for c in s:
            c1[ord(c) - ord('a')] += 1
        for c in t:
            c2[ord(c) - ord('a')] += 1
        return c1 == c2