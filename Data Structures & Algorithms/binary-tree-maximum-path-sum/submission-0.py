# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = [root.val]
        def maxPath(root):
            if not root:
                return 0  

            left = max(maxPath(root.left), 0)
            right = max(maxPath(root.right), 0)
            
            total[0] = max(total[0], root.val + left + right)
            return root.val + max(left, right)

        maxPath(root)
        return total[0]