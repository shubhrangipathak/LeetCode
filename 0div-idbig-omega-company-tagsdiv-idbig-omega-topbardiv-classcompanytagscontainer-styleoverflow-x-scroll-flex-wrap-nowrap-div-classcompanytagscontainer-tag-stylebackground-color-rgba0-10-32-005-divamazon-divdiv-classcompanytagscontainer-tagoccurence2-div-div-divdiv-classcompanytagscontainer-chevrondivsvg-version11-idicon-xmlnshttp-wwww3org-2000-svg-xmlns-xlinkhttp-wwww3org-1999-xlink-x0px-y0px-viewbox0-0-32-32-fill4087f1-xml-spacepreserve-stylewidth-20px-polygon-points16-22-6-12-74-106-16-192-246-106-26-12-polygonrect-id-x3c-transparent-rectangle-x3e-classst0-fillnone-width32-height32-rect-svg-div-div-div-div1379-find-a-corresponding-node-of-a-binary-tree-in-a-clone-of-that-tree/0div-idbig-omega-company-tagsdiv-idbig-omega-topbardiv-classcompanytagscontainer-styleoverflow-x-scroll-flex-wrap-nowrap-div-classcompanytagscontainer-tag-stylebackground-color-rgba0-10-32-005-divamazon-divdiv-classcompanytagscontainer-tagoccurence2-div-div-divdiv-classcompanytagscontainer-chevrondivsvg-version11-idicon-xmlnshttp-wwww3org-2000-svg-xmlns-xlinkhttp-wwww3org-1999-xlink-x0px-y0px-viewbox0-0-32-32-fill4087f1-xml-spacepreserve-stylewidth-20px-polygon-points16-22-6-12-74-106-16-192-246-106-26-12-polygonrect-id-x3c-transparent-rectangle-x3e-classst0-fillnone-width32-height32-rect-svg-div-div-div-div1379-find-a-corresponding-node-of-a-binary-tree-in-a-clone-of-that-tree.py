# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        queue = [cloned]
        while queue:
            n = len(queue)
            
            for i in range(n):
                currnode = queue.pop(0)
                if currnode.val == target.val:
                    return currnode
                
                if currnode.left:
                    queue.append(currnode.left)
                if currnode.right:
                    queue.append(currnode.right)
                    
        return cloned
            
            
           