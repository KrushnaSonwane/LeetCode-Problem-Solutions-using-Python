class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res, count, hashT = [], 0, defaultdict(int)
        for a, b in zip(A, B):
            hashT[a] += 1
            hashT[b] += 1
            if a != b:
                if hashT[a] == 2: count += 1
                if hashT[b] == 2: count += 1
            else:
                count += 1
            res.append(count)
        return res