class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        @cache
        def dfs(i, j, last, count):
            if count > limit: return 0
            if i == 0 and j == 0: return 1
            res = 0
            if i:
                res += dfs(i-1, j, 1, 0 + ((count + 1) if last == 1 else 1))
            if j:
                res += dfs(i, j-1, 0, 0 + ((count + 1) if last == 0 else 1))
            return res % (10**9+7)
        return (dfs(zero, one, 0, 0)) % (10**9+7)