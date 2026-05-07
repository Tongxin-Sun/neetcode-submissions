# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        nodes = []
        q1 = []
        while True:
            while q:
                curr = q.popleft()
                q1.append(curr.val)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
            q = deque(nodes)
            nodes = []
            res.append(q1)
            q1 = []
            if not q:
                break
        return res