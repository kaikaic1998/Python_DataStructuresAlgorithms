# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        carry = 0

        while l1 or l2 or carry:
            sum_num = 0
            if l1:
                sum_num = sum_num + l1.val
                l1 = l1.next
            if l2:
                sum_num = sum_num + l2.val
                l2 = l2.next
            sum_num += carry
            # carry = sum_num // 10
            carry, sum_num = divmod(sum_num, 10)
            newNode = ListNode(sum_num '''sum_num // 10''')
            tail.next = newNode
            tail = newNode

        return head.next