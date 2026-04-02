# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # node is a tree node, left and right are lower and upperbounds
        def isValid(node, lowerBound, upperBound):
            if not node:
                return True

            if not (lowerBound < node.val and upperBound > node.val):
                return False

            # lowerBound < node.left < node < node.right < right
            return isValid(node.left, lowerBound, node.val) and isValid(node.right, node.val, upperBound)

        return isValid(root, float("-inf"), float("+inf"))
        