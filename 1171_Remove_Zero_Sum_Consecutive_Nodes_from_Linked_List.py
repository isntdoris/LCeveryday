# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy

        while left is not None:
            cur_sum = 0
            right = left.next

            while right is not None:
                cur_sum += right.val
                if cur_sum == 0:
                    left.next = right.next
                right = right.next

            left = left.next
        return dummy.next     