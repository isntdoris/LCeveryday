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
            curr.next = prev # 改變pointer的方向
            prev = curr # 交換位置
            curr = nxt # 交換位置
        return prev