# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ";".join(res)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(";")
        if data[0] == "null":
            return None
        root = TreeNode(int(data[0]))
        q = deque([root])
        i = 1
        while q and i < len(data):
            node = q.popleft()
            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            if data[i + 1] != "null":
                node.right = TreeNode(int(data[i + 1]))
                q.append(node.right)

            i = i + 2

        return root
