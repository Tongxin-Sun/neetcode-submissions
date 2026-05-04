class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, ele in enumerate(nums):
            diff = target - ele
            if diff in hash_map:
                return [hash_map[diff], i] 
            hash_map[ele] = i