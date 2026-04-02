# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        prev = None
        carry = 0
        head = None
        while cur1 or cur2 or carry > 0:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            total = val1 + val2 + carry
            total_str = str(total)
            if len(total_str) > 1:
                carry = int(total_str[:-1])
                total = int(total_str[-1])
            else:
                carry = 0
            new = ListNode(total)
            if prev:
                prev.next = new
            if not head:
                head = new
            prev = new
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        return head