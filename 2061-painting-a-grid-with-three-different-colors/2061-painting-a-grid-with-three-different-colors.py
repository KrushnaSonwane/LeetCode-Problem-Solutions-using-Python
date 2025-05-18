class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j, left, s):
            if i == n: return 1
            if j == m: return dfs(i+1, 0, '3', s)
            res, MOD = 0, 10**9+7
            for color in '012':
                if color != left and color != s[j]:
                    res += dfs(i, j+1, color, s[:j] + color + s[j+1:])
            return res % MOD
        return dfs(0, 0, '3', '33333')