# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lcm = root
        def dfs(root):
            if p.val < root.val and q.val < root.val:
                dfs(root.left)
            if p.val > root.val and q.val > root.val:
                dfs(root.right)
            if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
                self.lcm = root
            if p.val == root.val or q.val == root.val:
                self.lcm = root
        dfs(root)
        return self.lcm

