# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        attach fake node to none, then create tail pointer that adds each node

        compare values of each linked list and based on attach it to tail
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
            
            else:
                tail.next = list1
                list1 = list1.next
                tail = tail.next

        tail.next = list1 or list2
        return dummy.next
        