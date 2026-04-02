# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, maximum):
            if not root:
                return 
            if root.val >= maximum:
                self.res += 1

            left = dfs(root.left, max(maximum, root.val))
            right = dfs(root.right, max(maximum, root.val))

        dfs(root, root.val)

        return self.res