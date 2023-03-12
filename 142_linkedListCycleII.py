# It is also called Hare-Tortoise algorithm
# The algorithm works by using two pointers, a slow pointer and a fast pointer.
# Initially, both pointers are set to the head of the linked list.
# The fast pointer moves twice as fast as the slow pointer.
# If there is a cycle in the linked list, eventually, the fast pointer will catch up with the slow pointer.
# If there is no cycle, the fast pointer will reach the end of the linked list.
class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    # Initialize two pointers, slow and fast, to the head of the linked list.
    slow = head
    fast = head

    # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
    # until they either meet or the fast pointer reaches the end of the list.
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next # twice the speed of slow pointer
      if slow == fast:
        # If the pointers meet, there is a cycle in the linked list.
        # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
        # until they meet again. The node where they meet is the starting point of the cycle.
        slow = head
        while slow != fast: # return when they meet again
          slow = slow.next
          fast = fast.next
        return slow

    # If the fast pointer reaches the end of the list without meeting the slow pointer,
    # there is no cycle in the linked list. Return None.
    return None