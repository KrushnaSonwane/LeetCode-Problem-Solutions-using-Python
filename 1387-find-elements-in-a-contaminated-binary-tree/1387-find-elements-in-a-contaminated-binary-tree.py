# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = set()
        def dfs(root, data):
            if not root: return
            self.arr.add(data)
            root.val = data
            dfs(root.left, (2 * root.val) + 1)
            dfs(root.right, (2 * root.val) + 2)
        dfs(root, 0)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.arr


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)