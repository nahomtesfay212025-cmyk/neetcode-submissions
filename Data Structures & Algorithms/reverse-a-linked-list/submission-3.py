# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1,2,3,4,5,None
        1.next = 2......5.next = None

        5,4,3,2,1,None
        1.next = None

        current should point to <- lets call it prev 
        nextnode = curr.next
        curr.next = prev
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
        