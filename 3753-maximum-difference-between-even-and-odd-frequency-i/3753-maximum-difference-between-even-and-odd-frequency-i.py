class Solution:
    def maxDifference(self, s: str) -> int:
        A = Counter(s)
        a1 = 0; a2 = inf
        for ch in A:
            if A[ch] % 2:
                a1 = max(a1, A[ch])
            else:
                a2 = min(a2, A[ch])
        # print(a, c,b, d)
        return a1 - a2