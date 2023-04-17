"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        depth = 1
        queue = [(root,depth)]
        while queue:
            root , depth = queue.pop(0)
            if root.children:
                for i in root.children:
                    queue.append([i,depth+1])
                    
        return depth