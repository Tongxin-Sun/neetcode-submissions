# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        def helper(node):
            nonlocal k
            if not node:
                return
            helper(node.left)
            if k == 1:
                self.res = node.val
            k -= 1
            helper(node.right)
        helper(root)
        return self.res
        
        