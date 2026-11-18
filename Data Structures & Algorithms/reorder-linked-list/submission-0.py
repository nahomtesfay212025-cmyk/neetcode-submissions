# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3 4 5 none
# 123  54
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        find mid value and split them in half 
        reverse the secend half 
        merge both
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        first = head
        second = slow.next
        slow.next = None
        
        curr = second
        prev = None
        while curr:
            currnext = curr.next
            curr.next = prev
            prev = curr
            curr = currnext

        
        dummy = ListNode()
        tail = dummy
        while first and prev:   #first = 1 ,2 ,3    prev = 5 ,4
            tail.next = first
            first = first.next
            tail = tail.next

            tail.next = prev
            prev = prev.next
            tail = tail.next
        
        tail.next = first or prev



            


        
        