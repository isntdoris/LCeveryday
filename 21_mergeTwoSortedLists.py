# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 神奇的方法一
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

# 使用merge的方法二（正宗）
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # First you initialize dummy and temp.
        # One is sitting at the start of the linkedlist and the other (temp) is going to move forward find which value should be added to the list.
        # Note that it's initialized with a value 0 but it can be anything! 
        curr = dummy = ListNode(0)

        while list1 and list2: # until one of them is empty               
            if list1.val < list2.val: # add the smaller of the two to the merged list
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
                
        if list1 or list2: # if one of the lists becomes none
            curr.next = list1 if list1 else list2
            
        return dummy.next # not too sure about this but it's supposed to return the new head of the merged linked list
        # 奇怪dummy在中間都沒被更新啊。。。
        # 解釋是這麼說: We return dummy.next since dummy is pointing to 0 and next to zero is what we've added throughout the process.

