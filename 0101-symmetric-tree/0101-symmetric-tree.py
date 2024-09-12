# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def comp(self, left, right):

        if not left and not right:
            return True
        
        if not left or not right:
            return False

        if left.val==right.val and self.comp(left.left, right.right) and self.comp(left.right, right.left):
            return True
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return 
        
        
        return self.comp(root.left, root.right)
            
        
