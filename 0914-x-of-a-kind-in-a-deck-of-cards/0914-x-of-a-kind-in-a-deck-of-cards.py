class Solution:
    def hasGroupsSizeX(self, A: List[int]) -> bool:
        hashT = Counter(A)
        A = sorted([hashT[num] for num in hashT])
        print(A)
        if A[0] < 2: return False
        for i in range(2, A[0] + 1):
            for num in A:
                if num % i != 0: break
            else:
                return True
        return False