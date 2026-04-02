"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def dfs(item):
            if item in oldToNew:
                return oldToNew[item]

            new = Node(item.val)
            oldToNew[item] = new

            for neighbor in item.neighbors:
                new.neighbors.append(dfs(neighbor))

            return new


        return dfs(node) if node else None

        


