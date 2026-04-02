"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        indices = {}
        cur = head
        while cur:
            indices[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        prev = None
        while cur:
            new = indices[cur]
            if prev:
                prev.next = new
            if cur.random:
                new.random = indices[cur.random] 
            else:
                new.random = None
            prev = new
            cur = cur.next

        return indices[head] 