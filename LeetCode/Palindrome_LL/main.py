# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def find_mid (head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse_LL (head):
            current = head
            prev = None
            nxt = None
            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev
        
        def compareLL (head, head2):
            while head and head2:
                if head.val != head2.val:
                    return False
                head = head.next
                head2 = head2.next
            return True

        mid = find_mid(head)
        head2 = reverse_LL(mid)

        return compareLL(head, head2)

        # self.front_pointer = head

        # def recursively_check(current_node=head):
        #     if current_node is not None:
        #         if not recursively_check(current_node.next):
        #             return False
        #         if self.front_pointer.val != current_node.val:
        #             return False
        #         self.front_pointer = self.front_pointer.next
        #     return True

        # return recursively_check()
        
        
