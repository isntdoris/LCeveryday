# 1. check if both nodes are none -> return true
# 2. check if only one none -> return false
# 3. check if the nodes have same values -> return true


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
            # 有點難理解這一行程式跑的順序，以及為什麼用and接在一起
        
        return isMirror(root, root)