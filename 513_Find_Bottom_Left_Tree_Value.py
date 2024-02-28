# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        maxD = -1
        ans = 0

        def search(node, d):
            if not node: return

            nonlocal maxD
            nonlocal ans
            if d > maxD:
                maxD = d
                ans = node.val
            search(node.left, d + 1)
            search(node.right, d + 1)
            return
        
        search(root, 0)
        return ans