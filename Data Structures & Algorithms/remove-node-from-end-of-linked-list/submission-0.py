# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        # we got length 
        freq = length - n 

        if freq == 0:
            return head.next

        curr = head
        for i in range(length - 1):
            if (i + 1) == freq:
                curr.next = curr.next.next
                break
            curr = curr.next
    
        # doesnt work fcor end of list removal n = 0
        return head