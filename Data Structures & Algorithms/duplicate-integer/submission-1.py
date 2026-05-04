class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        p1, p2 = 0, 1
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                return True
            p1 = p2
            p2 += 1
        return False