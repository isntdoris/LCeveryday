# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 我可以理解的方法一
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: 
        dummy = ListNode()
        tail = dummy

        while l1 != None and l2 != None: #1

            if l1.val < l2.val: #2
                tail.next = l1 #3
                l1 = l1.next #4
            else: 
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2  #5 taking the remaining portion and insert
        return dummy.next #6

# 神奇的方法二
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

# 使用merge的方法三（發現和方法一相同）
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # First you initialize dummy and tail.
        # One is sitting at the start of the linkedlist and the other (curr) is going to move forward find which value should be added to the list.
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
        # 奇怪dummy在中間都沒被更新啊。。。 ->  現在懂了 20230601
        # 解釋是這麼說: We return dummy.next since dummy is pointing to 0 and next to zero is what we've added throughout the process.