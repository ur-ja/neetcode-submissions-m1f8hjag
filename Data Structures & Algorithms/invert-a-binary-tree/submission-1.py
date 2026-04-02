# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        while stack:
            item = stack.pop()
            temp = item.left
            item.left = item.right
            item.right = temp
            if item.left:
                stack.append(item.left)
            if item.right:
                stack.append(item.right)

        return root

         