class Solution:
    def canPartitionGrid(self, A: List[List[int]]) -> bool:
        sum_ = sum(num for a in A for num in a)
        currSum = 0
        for j in range(len(A[0])):
            for i in range(len(A)):
                currSum += A[i][j]
            if currSum == sum_ - currSum: return True
        currSum = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                currSum += A[i][j]
            if currSum == sum_ - currSum: return True
        return False