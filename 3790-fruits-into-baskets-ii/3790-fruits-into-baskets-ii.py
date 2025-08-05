class Solution:
    def numOfUnplacedFruits(self, F: List[int], B: List[int]) -> int:
        res = len(F)
        for i in range(len(F)):
            for j in range(len(F)):
                if F[i] <= B[j]:
                    res -= 1
                    B[j] = 0
                    break
        return res