# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])

        # in pre order skip the elements that you know are to the left of root 
        # on the basis of in order
        # in order just keep the nodes to the left of root
        root.left = self.buildTree(preorder[1: root_index + 1], inorder[:root_index]) 
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])

        return root