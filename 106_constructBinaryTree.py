# Algorithm
# 1. Build hashmap value -> its index for inorder traversal.
# 2. Return helper function which takes as the arguments the left and right boundaries for the current subtree in the inorder traversal.
# These boundaries are used only to check if the subtree is empty or not. Here is how it works helper(in_left = 0, in_right = n - 1):
#       - If in_left > in_right, the subtree is empty, return None.
#       - Pick the last element in postorder traversal as a root.
#       - Root value has index index in the inorder traversal, elements from in_left to index - 1 belong to the left subtree, and elements from index + 1 to in_right belong to the right subtree.
#       - Following the postorder logic, proceed recursively first to construct the right subtree helper(index + 1, in_right) and then to construct the left subtree helper(in_left, index - 1).
#       - Return root.

# I don't understand why in_left > in_right, the subtree is empty, return None.

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right): 
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]

            # use helper to call helper, thus create recursion
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)

            return root

        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1) # it's clever to be able to return root via helper function

