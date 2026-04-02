# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i - 1], lists[i])

        return lists[-1]

    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            print(list1.val)
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            print(list2.val)
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
