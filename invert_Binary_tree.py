'''
Invert a binary tree. 
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to   4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
 This problem was inspired by this original tweet by Max Howell: 
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
'''
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:            
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        (root.left,root.right) = (root.right, root.left)
        return root    
            
