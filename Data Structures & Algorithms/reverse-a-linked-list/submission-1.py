# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if list is empty it cannot be reversed
        # base case
        if not head:
            return None

        # base value will be start of list
        newHead = head

        if head.next:
            # recirsive call to find the end of the list and update the result list
            newHead = self.reverseList(head.next)

            # set the next val of the next node to the current node to reverse it
            # since linked lists use pointers this will update newHead
            head.next.next = head

        # to mark end of list
        head.next = None

        return newHead
