# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        use two pointers slow and right and if they are able to be same then return true  
        """
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False
        