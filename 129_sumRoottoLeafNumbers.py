# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# intuition
# 1. Push root into stack.
# 2. While stack is not empty:
# 3. Pop out a node from stack and update the current number.
# 4. If the node is a leaf, update root-to-leaf sum.
# 5. Push right and left child nodes into stack.
# 6. Return root-to-leaf sum.

class Solution: #DFS preorder approach
    def sumNumbers(self, root: TreeNode):
        root_to_leaf = 0
        stack = [(root, 0) ]
        
        while stack: # while stack is not empty
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))
                        
        return root_to_leaf