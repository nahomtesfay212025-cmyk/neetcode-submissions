# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        0 - 1- 2- 3- none
        3-2-1- 0 -none
        initiate prev as none
        start curr with your head
        nextnode = curr.next
        curr.next = prev.  0-none
        prev = curr
        curr = nextnode


        """

        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev

        