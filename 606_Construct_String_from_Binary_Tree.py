# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def helper(node):
            if not node:
                return

            res.append('(')
            res.append(str(node.val))
            if not node.left and node.right: # RICKY HERE
                res.append('()')
            helper(node.left)
            helper(node.right)
            res.append(')')

        helper(root)
        return ''.join(res)[1:-1] # RICKY HERE