"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        create empty dictionary that maps original node with copied node
        attach each node in accordance for both next and random
        """
        copies = {}
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copies[curr].next = copies.get(curr.next)
            copies[curr].random = copies.get(curr.random)
            curr = curr.next

        return copies.get(head)
        
        
        