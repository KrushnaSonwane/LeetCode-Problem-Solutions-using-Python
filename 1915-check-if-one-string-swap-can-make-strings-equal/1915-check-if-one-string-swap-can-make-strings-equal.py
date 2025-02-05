class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        res = []
        for i, (ch1, ch2) in enumerate(zip(s1, s2)):
            if ch1 != ch2: res.append(i)
        if not res: return True
        if len(res) != 2: return False
        if s1[res[0]] != s2[res[1]] or s2[res[0]] != s1[res[1]]: return False
        return True