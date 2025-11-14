class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2 + 1):
                if col1 - 1 >= 0: res[i][col1 - 1] -=1
                res[i][col2] += 1
        for i in range(n):
            last = 0 
            for j in range(n - 1, -1, -1):
                res[i][j] += last
                last = res[i][j]
        return res