# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root, array):
            if not root:
                return array
            
            inorder(root.left, array)
            array.append(root.val)
            inorder(root.right, array)

            return array
        result = inorder(root, [])
        return result[k - 1]

    




