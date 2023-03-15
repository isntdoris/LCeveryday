# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach : Breadth First Search
# Traverse the tree in level-order using a queue. At each level, we add the left and right child nodes of each node to the queue.
# If we encounter a null node, we still add it to the queue so that we can check if there are any more nodes left in the next step.
# Once we have traversed the entire tree, we check if there are any remaining nodes in the queue.
# If there are, it means the tree is not complete, and we return false.
# Otherwise, the tree is complete, and we return true.
        
from collections import deque

# 方法一（稍稍慢）
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # Check if the root node is None, if so, return True (an empty tree is complete)
        if not root:
            return True

        # Create a deque to store the nodes of the tree in level order
        q = deque([root])

        # Traverse the tree in level order
        while q[0] is not None:
            # Remove the first node from the deque
            node = q.popleft()
            # Add the left and right child nodes of the current node to the deque
            q.append(node.left)
            q.append(node.right)

        # Remove any remaining None nodes from the beginning of the deque
        while q and q[0] is None:
            q.popleft()

        # Check if there are any remaining nodes in the deque
        # If so, the tree is not complete, so return False
        # Otherwise, the tree is complete, so return True
        return not bool(q) # 此condition欲確認如果為假（空）return True

# 方法二（比較快）
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = [root]

        flag = False

        while q:
            node = q.pop(0)

            if node is None:
                flag = True
                continue
            
            if flag:
                return False

            q.append(node.left)
            q.append(node.right)

        return True            