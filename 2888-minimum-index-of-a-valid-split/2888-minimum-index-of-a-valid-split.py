from sortedcontainers import SortedList
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right = collections.Counter(nums)
        max_ = max(right.values())
        for val in right:
            if right[val] == max_:
                res = val
        l, r = defaultdict(int), right
        for i, num in enumerate(nums):
            l[num] += 1
            r[num] -= 1
            if l[res] * 2 > i+1 and r[res] * 2 > len(nums)-i-1: return i
        return -1