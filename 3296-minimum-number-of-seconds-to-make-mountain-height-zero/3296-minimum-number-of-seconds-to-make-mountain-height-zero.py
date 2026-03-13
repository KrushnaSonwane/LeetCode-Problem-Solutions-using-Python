class Solution:
    def minNumberOfSeconds(self, k: int, A: List[int]) -> int:

        def solve(mid, lim):
            for num in A:
                count = 1; sum_ = 0
                while num * count + sum_ <= mid:
                    lim -= 1; sum_ += num * count
                    count += 1
                    if lim == 0: return True
            return lim == 0
                

        l, r = 0, 10**17
        ans = 0
        while r >= l:
            mid = (l + r) // 2
            if solve(mid, k):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans