# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1, fast but not using merge sort (I think)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        for i in lists:
            x = i
            while x:
                temp += [x.val]
                x = x.next
        
        temp = sorted(temp, reverse=True)
        ans = None
        for i in temp:
            ans = ListNode(i, ans)
        return ans

# solution 2, slow but using merge sort (divide and conquer)
# Intuition of this Problem:
# This solution uses the merge sort algorithm to merge all the linked lists in the input vector into a single sorted linked list. The merge sort algorithm works by recursively dividing the input into halves, sorting each half separately, and then merging the two sorted halves into a single sorted output.

# Approach for this Problem:
# 1. Define a function merge that takes two pointers to linked lists as input and merges them in a sorted manner.
# a. Create a dummy node with a value of -1 and a temporary node pointing to it.
# b. Compare the first node of the left and right linked lists, and append the smaller one to the temporary node.
# c. Continue this process until either of the lists becomes empty.
# d. Append the remaining nodes of the non-empty list to the temporary node.
# e. Return the next node of the dummy node.

# 2. Define a function mergeSort that takes three arguments - a vector of linked lists, a starting index, and an ending index. It performs merge sort on the linked lists from the starting index to the ending index.
# a. If the starting index is equal to the ending index, return the linked list at that index.
# b. Calculate the mid index and call mergeSort recursively on the left and right halves of the vector.
# c. Merge the two sorted linked lists obtained from the recursive calls using the merge function and return the result.

# 3. Define the main function mergeKLists that takes the vector of linked lists as input and returns a single sorted linked list.
# a. If the input vector is empty, return a null pointer.
# b. Call the mergeSort function on the entire input vector, from index 0 to index k-1, where k is the size of the input vector.
# c. Return the merged linked list obtained from the mergeSort function call.
# End of algorithm.

class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(-1)
        temp = dummy
        while left and right:
            if left.val < right.val:
                temp.next = left
                temp = temp.next
                left = left.next
            else:
                temp.next = right
                temp = temp.next
                right = right.next
        while left:
            temp.next = left
            temp = temp.next
            left = left.next
        while right:
            temp.next = right
            temp = temp.next
            right = right.next
        return dummy.next
    
    def mergeSort(self, lists: List[ListNode], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)
        return self.merge(left, right)
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)