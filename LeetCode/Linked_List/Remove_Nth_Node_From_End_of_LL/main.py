# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # solution with one function pass
        dummy = ListNode()
        dummy.next = head

        fast = dummy
        slow = dummy

        for i in range(0, n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next

        # solution with two function pass
        # length = 0
        # dummy = ListNode()
        # dummy.next = head
        # first_node = head

        # while first_node:
        #     length += 1
        #     first_node = first_node.next
        
        # length -= n
        # first_node = dummy

        # while length > 0:
        #     length -= 1
        #     first_node = first_node.next
        # first_node.next = first_node.next.next

        # return dummy.next