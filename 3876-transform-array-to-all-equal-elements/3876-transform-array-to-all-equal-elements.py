class Solution:
    def canMakeEqual(self, A: List[int], k: int) -> bool:
        def solve(match):
            count = 0
            last = 0
            for i in range(len(A)-1):
                if A[i] == match and last == 0: 
                    continue
                if A[i] != match and last: 
                    last = 0
                    continue
                last = 1
                count += 1
            if A[-1] == match and last == 0 and count <= k:
                return True
            if A[-1] != match and last and count <= k:
                return True
            return False
        return solve(-1) or solve(1)