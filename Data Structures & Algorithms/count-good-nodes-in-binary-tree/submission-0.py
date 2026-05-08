# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxVal):
            if not root:
                return 0
            currentMax = max(maxVal, root.val)
            left = helper(root.left, currentMax)
            right = helper(root.right, currentMax)
            curr = root.val >= maxVal
            return left + right + curr
        return helper(root, root.val)