# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=float('-inf'), upper=float('inf')) -> bool:
        if not root: 
            return True

        if root.val <= lower or root.val >= upper: 
            return False

        if not root.left: 
            pass
        
        elif root.val <= root.left.val:
            return False
        
        if not root.right:
            pass
        elif root.val >= root.right.val: 
            return False

        return self.isValidBST(root.left, lower=lower, upper=root.val) and self.isValidBST(root.right, lower=root.val , upper=upper)