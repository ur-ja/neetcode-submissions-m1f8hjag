# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = root.val
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            # update res if splitting is greater
            self.res = max(left + right + node.val, self.res)

            # return max of left, right or node
            return max(left + node.val, right + node.val, node.val)

        dfs(root)
        return self.res
                