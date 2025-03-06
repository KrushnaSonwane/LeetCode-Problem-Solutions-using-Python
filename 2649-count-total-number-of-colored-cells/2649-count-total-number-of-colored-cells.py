class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        curr = 4
        while n - 1:
            res += curr
            curr += 4
            n -= 1
        return res