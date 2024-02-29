"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def height(node):
            nonlocal diameter
            max_diameter_1, max_diameter_2 = 0, 0
            
            if len(node.children) == 0:
                return 0
            
            # RICKY HERE
            for child in node.children:
                parent_diameter = height(child) + 1
                if parent_diameter > max_diameter_1:
                    max_diameter_1, max_diameter_2 = parent_diameter, max_diameter_1
                elif parent_diameter > max_diameter_2:
                    max_diameter_2 = parent_diameter
                
                distance = max_diameter_1 + max_diameter_2
                diameter = max(diameter, distance)
  
            return max_diameter_1
            
        height(root)
        return diameter