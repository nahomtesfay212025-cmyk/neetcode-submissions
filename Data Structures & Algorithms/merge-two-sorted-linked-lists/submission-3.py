# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        create a dummy node which is a fake node and points to none
        lets use tail pointer that adds nodes based on the codition
        so while loop of both lists(only when both exist)
        comapre correspending values of linked list and add node with the smallest value to tail and move that linked list to next pointer move tail to next node too

        """

        dummy = ListNode(0)
        dummy.next = None
        tail = dummy

        while list1 and list2:
            if list1.val> list2.val:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
            else:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
        
        tail.next = list1 or list2
        return dummy.next