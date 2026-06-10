# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ll_copy = []
        while curr:
            ll_copy.append(curr.val)
            curr = curr.next
        ll_copy = ll_copy[::-1]
        if ll_copy == []:
            return head
        new_head = ListNode(ll_copy[0])
        curr = new_head
        for ele in ll_copy[1:]:
            curr.next = ListNode(ele)
            curr = curr.next
        return new_head
            

        