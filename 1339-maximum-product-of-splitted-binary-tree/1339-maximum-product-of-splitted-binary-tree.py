# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum_ = 0
        def getSum(root):
            if not root: return
            getSum(root.left)
            self.sum_ += root.val
            getSum(root.right)
        getSum(root)
        self.ans = 0
        def dfs(root, curr):
            if not root: return 0
            curr = dfs(root.left, curr) + dfs(root.right, curr) + root.val
            self.ans = max(self.ans, curr * (self.sum_ - curr))
            return curr
        dfs(root, 0)
        return self.ans % ((10**9) + 7)