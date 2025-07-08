class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        end = [v for v, _, _ in events]
        @cache
        def dfs(i, k):
            if not k or i == len(events): return 0
            res = dfs(i+1, k)
            j = bisect.bisect_right(end, events[i][1])
            res = max(res, dfs(j, k - 1) + events[i][2])
            return res
        return dfs(0, k)