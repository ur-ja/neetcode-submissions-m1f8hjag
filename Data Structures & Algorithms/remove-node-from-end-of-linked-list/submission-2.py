# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        cur = head
        i = 0
        idx = length  - n

        prev = None
        while cur and i <= idx:
            print(i, idx)
            if i == idx:
                if i == 0:
                    return head.next
                prev.next = prev.next.next
            prev = cur
            cur = cur.next
            i += 1

        return head

