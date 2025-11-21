class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        allCh = "abcdefghijklmnopqrstuvwxyz"
        res = 0
        for ch in allCh:
            i, j = 0, len(s)-1
            while i < len(s) and s[i] != ch:
                i += 1
            while j >= 0 and s[j] != ch:
                j -= 1
            hashT = set()
            for ii in range(i+1, j):
                hashT.add(s[ii])
            res += len(hashT)
        return res