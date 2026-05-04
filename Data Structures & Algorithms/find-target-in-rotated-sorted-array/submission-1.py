class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                if nums[l] == nums[r]:
                    return l
                m = (l + r) // 2
                if nums[m] <= nums[r]:
                    r = m
                else:
                    l = m + 1
        minIndex = findMin(nums)
        if target > nums[-1]:
            l, r = 0, minIndex - 1
        else:
            l, r = minIndex, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1