class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:

            if not self.isAlphanumeric(s[l]):
                l += 1
                continue
            
            if not self.isAlphanumeric(s[r]):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True

    def isAlphanumeric(self, char):
        if ord("a") <= ord(char.lower()) <= ord("z") or ord("0") <= ord(char.lower()) <= ord("9"):
            return True
        return False