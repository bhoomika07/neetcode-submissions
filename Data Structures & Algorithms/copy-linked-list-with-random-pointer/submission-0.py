"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        hash_map = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            hash_map[curr] = copy
            curr = curr.next
        
        temp = Node(0)
        curr1 = temp
        curr = head
        while curr:
            curr1.next = hash_map[curr]
            curr1 = curr1.next
            curr1.random = hash_map[curr.random]
            curr = curr.next
        return temp.next
        