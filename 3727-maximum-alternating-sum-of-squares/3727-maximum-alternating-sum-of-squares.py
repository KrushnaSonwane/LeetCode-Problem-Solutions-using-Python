class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        A = []
        for num in nums:
            A.append(num**2)
        A.sort()
        ans = A[-1]
        l, r = 0, len(A)-2
        flag = False
        while r >= l:
            if flag:
                ans += A[r]
                r -= 1
            else:
                ans -= A[l]
                l += 1
            flag = not flag
        return ans