# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode(0)
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        cur = result
        while minHeap:
            minimum = heapq.heappop(minHeap)
            cur.next = minimum[2]
            cur = cur.next
            nxt = minimum[2].next
            if nxt:
                heapq.heappush(minHeap, (nxt.val, minimum[1], nxt))

        return result.next

