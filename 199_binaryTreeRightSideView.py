# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = deque()

        if root:
            q.append(root)
        
        level = 0
        while len(q) > 0:
            res.append(q[-1].val)

            for i in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1
            
        return res

        # ans = []
        # if not root:
        #     return ans
        
        # q = [root]
        
        # while q:
        #     lv = []
            
        #     ans.append(q[-1].val)
            
        #     for node in q:
        #         if node.left:
        #             lv.append(node.left)
        #         if node.right:
        #             lv.append(node.right)
            
        #     q = lv
        
        # return ans