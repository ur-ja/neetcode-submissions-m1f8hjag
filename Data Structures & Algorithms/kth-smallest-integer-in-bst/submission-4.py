# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.res = root.val

        def bst(node):
            if node.left:
                bst(node.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                return
            if node.right:
                bst(node.right)
                
        bst(root)
        return self.res 