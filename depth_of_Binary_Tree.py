'''
104. Maximum Depth of Binary Tree 
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        right = 0
        left = 0
        if not root:
            return 0
        
        
       
        if root.left != 'None':        
            left = self.maxDepth(root.left)            
        
        if root.right != 'None':            
            right = self.maxDepth(root.right)
        
        return 1 + max(left,right)