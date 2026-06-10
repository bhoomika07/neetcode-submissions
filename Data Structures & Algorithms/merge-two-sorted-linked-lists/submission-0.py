# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        dummy = ListNode(0)
        curr = dummy     
        while c1 and c2:
            if c1.val < c2.val:
                curr.next = c1
                c1 = c1.next
                curr = curr.next
            elif c2.val < c1.val:
                curr.next = c2
                c2 = c2.next
                curr = curr.next
            elif c1.val == c2.val:
                curr.next = c1
                c1 = c1.next
                curr = curr.next
                curr.next = c2
                c2 = c2.next
                curr = curr.next
        while c1:
            curr.next = c1
            c1 = c1.next
            curr = curr.next
        while c2:
            curr.next = c2
            c2 = c2.next
            curr = curr.next
        return dummy.next

        