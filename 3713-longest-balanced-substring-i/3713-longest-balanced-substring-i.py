class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            hashT = defaultdict(int)
            for j in range(i, len(s)):
                hashT[s[j]] += 1
                if min(hashT.values()) == max(hashT.values()):
                    res = max(res, j - i + 1)
        return res