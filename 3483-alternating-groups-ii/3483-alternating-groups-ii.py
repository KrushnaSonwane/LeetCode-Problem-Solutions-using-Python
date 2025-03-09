class Solution:
    def numberOfAlternatingGroups(self, A: List[int], k: int) -> int:
        i = 0
        last = 0
        for i in range(k-2):
            if A[i] == A[i+1]:
                last = i+1
        res = 0
        j = k-1
        n = len(A)
        for i in range(len(A)):
            if A[j%n] == A[(j-1)%n]:
                last = j
            if last <= i:
                res += 1
            j += 1
        return res
                