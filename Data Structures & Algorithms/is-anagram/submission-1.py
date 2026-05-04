class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.charArray(s) == self.charArray(t):
            return True
        return False

    def charArray(self, s: str):
        char_arr = [0] * 26

        for char in s:
            char_arr[ord(char.lower()) - ord("a")] += 1

        return char_arr
        