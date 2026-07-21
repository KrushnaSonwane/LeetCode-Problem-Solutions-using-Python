class Solution:
    def maxActiveSectionsAfterTrade(self, A: str) -> int:
        count = A.count('1')
        i, res, first, second = 0, 0, 0, 0
        while i != len(A):
            while i != len(A) and A[i] == '1':
                i += 1
            first = second; second = 0
            while i != len(A) and A[i] == '0':
                second += 1
                i += 1
            if first != 0 and second != 0:
                res = max(res, first + second)
        return res + count