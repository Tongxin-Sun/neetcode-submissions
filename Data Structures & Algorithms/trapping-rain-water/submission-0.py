class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix, res = [0] * len(height), [0] * len(height), 0
        for i in range(1, len(prefix)):
            prefix[i] = max(prefix[i - 1], height[i - 1])

        for i in range(len(suffix) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])
            res += max(min(suffix[i], prefix[i]) - height[i], 0)
        return res