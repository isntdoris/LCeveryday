# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # measure 1 (optimal): using 2 pointers
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev # 不理解這個步驟
            prev = curr
            curr = nxt
        return prev