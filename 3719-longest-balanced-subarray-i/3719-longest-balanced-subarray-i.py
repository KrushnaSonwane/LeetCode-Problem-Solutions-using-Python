class Solution:
    def longestBalanced(self, A: List[int]) -> int:
        res = 0
        for i in range(len(A)):
            even, odd = set(), set()
            for j in range(i, len(A)):
                if A[j] % 2:
                    odd.add(A[j])
                else: even.add(A[j])
                if len(even) == len(odd):
                    res = max(res, j - i + 1)
        return res