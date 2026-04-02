# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maximum):
            res = 0
            if not root:
                return res
            if root.val >= maximum:
                res = 1
            res += dfs(root.left, max(maximum, root.val))
            res += dfs(root.right, max(maximum, root.val))
            return res

        return dfs(root, root.val)