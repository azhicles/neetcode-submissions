# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    res = None
    count = 0 
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.search(root, k)
    
    def search(self, node, k):
            
            if node.left:
                self.res = self.search(node.left, k)
                
            self.count += 1
            if self.count == k: 
                return node.val
            
            if node.right: 
                self.res = self.search(node.right, k)
                
            return self.res
            
