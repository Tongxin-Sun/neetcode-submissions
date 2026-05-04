class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums.sort()

        longest = 1
        currentLength = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                currentLength += 1
            elif nums[i] - nums[i - 1] > 1:
                currentLength = 1

            longest = max(currentLength, longest) 

        return longest