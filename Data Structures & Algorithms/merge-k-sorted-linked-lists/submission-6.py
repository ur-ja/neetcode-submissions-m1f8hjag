# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeLists(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next

        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next

        return dummy.next

            