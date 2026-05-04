# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0

        def getHeight(node):
            if not node:
                return -1
            left = getHeight(node.left)
            right = getHeight(node.right)
            self.maxLength = max(self.maxLength, left + right + 2)
            return max(left, right) + 1

        getHeight(root)

        return self.maxLength