class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def solve(last, ch, i, res):
            curr = 0
            while i < len(s) and ch == s[i]:
                curr += 1
                if last >= curr:
                    res += 1
                i += 1
            return curr, i, res
        i, curr, res = 0, 0, 0
        while i < len(s):
            curr, i, res = solve(curr, s[i], i, res)
        return res

        