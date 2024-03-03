# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxSeen):
            nonlocal cnt
            if node.val >= maxSeen:
                cnt += 1
            if node.left:
                dfs(node.left, max(node.val, maxSeen))
            if node.right:
                dfs(node.right, max(node.val, maxSeen))

        cnt = 0
        dfs(root, float('-inf'))
        return cnt