# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        # prev, curr, second, nxtPair, curr.next, curr.next.next (6 variables)

        while curr and curr.next:
            # save pointers
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pair
            curr.next = nxtPair
            second.next = curr
            prev.next = second

            # update pointers
            prev = curr
            curr = nxtPair
        
        return dummy.next