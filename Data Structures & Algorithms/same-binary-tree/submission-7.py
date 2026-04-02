# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            nodeP = q1.popleft()
            nodeQ = q2.popleft()

            if not nodeP and not nodeQ:
                continue
            elif nodeP and nodeQ and nodeP.val == nodeQ.val:
                q1.append(nodeP.left)
                q2.append(nodeQ.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.right)
            else:
                return False
        
        return True

            
