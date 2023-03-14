# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = []

        x = list1
        while x:
            temp += [x.val]
            x = x.next
        
        x = list2
        while x:
            temp += [x.val]
            x = x.next
        
        temp = sorted(temp, reverse=True)
        ans = None
        for i in temp:
            ans = ListNode(i, ans)
        return ans