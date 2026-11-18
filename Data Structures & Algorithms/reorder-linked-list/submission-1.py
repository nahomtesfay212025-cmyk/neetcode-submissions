# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0   1   2   3
          6   5    4

          1, create two linked list
          use slow and fast to get the middle node
          for the first node 
          store second = slow.next   4-5-6-none
          make slow.next to be none so that we have 
          first = 0-1-2-3-none


          2,reverse the 2nd linked list
          prev = none
          curr = second and reverse it

          3, merge first with reversed second
          first and prev then add them to dummy fake node
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        first = head
        slow.next = None

        prev = None
        curr = second
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        dummy = ListNode(0)
        tail = dummy

        while first and prev:
            tail.next = first
            tail = tail.next
            first = first.next

            tail.next = prev
            tail = tail.next
            prev = prev.next

        tail.next = first or prev
         












        