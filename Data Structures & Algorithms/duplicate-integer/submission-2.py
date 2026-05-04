class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()
        for n in nums:
            if n in counts:
                return True
            counts.add(n)
        return False