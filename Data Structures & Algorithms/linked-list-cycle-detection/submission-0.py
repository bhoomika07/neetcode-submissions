# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        hash_map = {}
        while curr:
            if curr.next not in hash_map:
                hash_map[curr.next] = 0
            else:
                return True
            curr = curr.next
        return False
        