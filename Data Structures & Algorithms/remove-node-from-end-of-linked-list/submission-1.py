# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4,5] n = 2
        # [1,2,3,5] len(nums) - n + 1
        if head is None or head.next is None:
            return None
        count = 0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        position = count - n + 1
        if position == 1:
            return head.next
        curr = head
        for i in range(1,position-1):
            curr = curr.next
        next_node = curr.next
        curr.next = next_node.next
        return head


        