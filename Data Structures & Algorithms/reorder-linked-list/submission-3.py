# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        def reverse(head: Optional[ListNode]):
            curr = head
            prev = None
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        slow_reversed = reverse(slow)
        curr1 = head
        curr2 = slow_reversed
        temp = ListNode(0)
        dummy = temp
        while curr1 and curr2:
            temp.next = curr1
            curr1 = curr1.next
            temp = temp.next
            temp.next = curr2
            curr2 = curr2.next
            temp = temp.next

        
        while curr1:
            temp.next = curr1
            curr1 = curr1.next
            temp = temp.next 
        while curr2:
            temp.next = curr2
            curr2 = curr2.next
            temp = temp.next 
        