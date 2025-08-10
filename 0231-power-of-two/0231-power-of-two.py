class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def dfs(num):
            if num == 1: return True
            if num % 2 or 0 >= num: return False
            return dfs(num//2)
        return dfs(n)