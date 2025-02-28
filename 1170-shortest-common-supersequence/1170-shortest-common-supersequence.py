class Solution:
    def shortestCommonSupersequence(self, A: str, B: str) -> str:
        @cache
        def dfs(i, j):
            if i == len(A): return B[j:]
            if j == len(B): return A[i:]
            if A[i]==B[j]:
                res = A[i]+dfs(i+1, j+1)
            else:
                res = A[i] + dfs(i+1, j)
                res2 = B[j] + dfs(i, j+1)
                if len(res)>len(res2): return res2
            return res
        return dfs(0, 0)