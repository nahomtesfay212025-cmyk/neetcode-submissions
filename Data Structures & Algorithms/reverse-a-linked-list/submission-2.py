# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        prev = None
        curr = head
        1 - 2 - 3 - 4 - 5 - None
        1.next = 2
        5.next = None

        5 - 4 - 3 - 2 - 1 - None
        1.next = None

        nextcurr = curr.next
        curr.next = prev

        prev = curr
        curr = currnext

    
        """
        prev = None
        curr = head
        while curr:
            nextcurr = curr.next
            curr.next = prev
            prev = curr
            curr = nextcurr
        return prev
       