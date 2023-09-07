# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lvlCnt = defaultdict(int)
        lvlSum = defaultdict(int)

        def helper(node, level):
            if not node:
                return
            lvlCnt[level] += 1
            lvlSum[level] += node.val

            helper(node.left, level + 1)
            helper(node.right, level + 1)


        helper(root, 0)

        return [lvlSum[i] / lvlCnt[i] for i in range(len(lvlCnt))]