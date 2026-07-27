# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # split the lists into two parts
        i = 1

        curr = head
        prev_left = None

        while i < left:
            prev_left = curr
            curr = curr.next
            i += 1
        temp = curr 

        curr = temp
        while i < right:
            curr = curr.next
            i+=1
        next_node = curr.next
        curr.next = None

        def _reverse(head: Optional[ListNode]):
            curr = head
            prev = None
            while curr:
                next_node = curr.next
                curr.next = prev
                prev= curr
                curr = next_node
            return prev
        reversed_half = _reverse(temp)
        curr1 = reversed_half
        while curr1 and curr1.next:
            curr1 = curr1.next
        curr1.next = next_node
        if prev_left:
            prev_left.next = reversed_half
            return head
        return reversed_half

        