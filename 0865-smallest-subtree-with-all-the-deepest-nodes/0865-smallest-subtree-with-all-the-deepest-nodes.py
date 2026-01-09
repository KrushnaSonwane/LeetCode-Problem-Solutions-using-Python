# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def getHeight(root):
            if not root: return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1
        
        def solve(root):
            if not root: return
            l = getHeight(root.left)
            r = getHeight(root.right)
            
            if l == r: return root
            elif r > l: return solve(root.right)
            else: return solve(root.left)
        return solve(root)