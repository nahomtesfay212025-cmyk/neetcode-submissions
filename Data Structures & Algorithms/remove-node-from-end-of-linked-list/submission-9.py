# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 0
        # curr = head

        # while curr:
        #     length += 1
        #     curr = curr.next

        # dummy = ListNode(0, head)
        # curr = dummy
        
        # for i in range(length - n):
        #     curr = curr.next
        
        # curr.next = curr.next.next
        # return dummy.next
        """
        dummy123456  n = 2
        """
        dummy = ListNode(0, head)
        
        fast = dummy

        for i in range(n):
            fast = fast.next

        slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next














