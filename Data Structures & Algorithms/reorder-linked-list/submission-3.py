# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        prev = slow.next = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # prev is the head of the reversed list 
        second = prev
        cur = head
        # merge two halves
        while second:
            first_next = cur.next
            second_next = second.next
            cur.next = second
            second.next = first_next
            cur = first_next
            second = second_next