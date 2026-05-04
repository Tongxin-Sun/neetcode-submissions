class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(value, index) for index, value in enumerate(nums)], key = lambda x: x[0])
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            total = nums[p1][0] + nums[p2][0]
            if total == target:
                if nums[p1][1] <= nums[p2][1]:
                    return [nums[p1][1], nums[p2][1]]
                else:
                    return [nums[p2][1], nums[p1][1]]
            elif total > target:
                p2 -= 1
            else:
                p1 += 1
