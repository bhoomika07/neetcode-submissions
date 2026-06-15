# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        array = []
        while curr:
            array.append(curr.val)
            curr = curr.next

        final = []
        left = 0
        right = len(array) - 1
        while left <= right:
            if array[left] == array[right]:
                final.append(array[left])
            else:
                final.append(array[left])
                final.append(array[right])
            left+=1
            right-=1
        curr = head
        for ele in final:
            curr.val = ele
            curr = curr.next



        