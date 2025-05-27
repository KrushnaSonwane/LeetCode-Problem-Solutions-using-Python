class Solution:
    def findCommonResponse(self, R: List[List[str]]) -> str:
        hashT= Counter()
        for A in R:
            A = set(A)
            for word in A: hashT[word] += 1
        max_, res = 0, ''
        max_ = max(hashT.values())
        for word in hashT:
            if max_ == hashT[word]:
                if not res: res = word
                else: res = min(res, word)
        return res