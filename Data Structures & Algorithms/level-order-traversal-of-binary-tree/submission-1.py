# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque();

        if root:
            queue.append(root)
        result = [];
        while queue:
            level = [];
            for i in range(len(queue)):
                topNode = queue.popleft()
                level.append(topNode.val)
                if topNode.left:
                    queue.append(topNode.left)
                if topNode.right:
                    queue.append(topNode.right)
            result.append(level)

        return result


