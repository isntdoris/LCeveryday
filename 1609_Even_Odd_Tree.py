# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        q = deque([root])

        while q:
            prev = float('-inf') if even == True else float('inf')
            for _ in range(len(q)):
                curr = q.popleft()

                if even and (curr.val % 2 == 0 or curr.val <= prev): return False
                elif not even and (curr.val % 2 == 1 or curr.val >= prev): return False

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                prev = curr.val
            
            even = not even
        return True