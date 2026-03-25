class Solution:
    def canPartitionGrid(self, A: List[List[int]]) -> bool:
        sum_ = sum(num for a in A for num in a)
        def solve(a, b, currSum, rev):
            for i in range(a):
                for j in range(b):
                    currSum += A[i if rev else j][j if rev else i]
                if currSum == sum_ - currSum: return True
            return False
        return solve(len(A[0]), len(A), 0, 0) or solve(len(A), len(A[0]), 0, 1)