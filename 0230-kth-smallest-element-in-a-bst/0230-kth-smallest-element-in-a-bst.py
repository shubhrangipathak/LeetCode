# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
    
        tree_list = inorder(root)
        
        return tree_list[k-1]