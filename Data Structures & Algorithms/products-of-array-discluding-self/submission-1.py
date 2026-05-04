class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            prefix = res[i] = prefix * nums[i - 1]
        
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            res[i] *= postfix
            
        return res