# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        orderedList = [];
        def inOrderTraversal(root):
            if not root:
                return

            if root.left:
                inOrderTraversal(root.left)
            if root.val is not None:
                orderedList.append(root.val)
            if root.right:
                inOrderTraversal(root.right)
        
        inOrderTraversal(root)
        return orderedList[k-1]
                

        