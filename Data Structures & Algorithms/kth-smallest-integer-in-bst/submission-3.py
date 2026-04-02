# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [] 

        def bst(root):
            if root.left:
                bst(root.left)
            res.append(root.val)
            if root.right:
                bst(root.right)
                
        bst(root)
        return res[k - 1] 