class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        arr = []
        count = 0
        for li in grid:
            for num in li: arr.append(num)
        arr.sort()
        mid = arr[len(arr) // 2]
        for num in arr:
            diff = abs(mid - num)
            if diff % x != 0: return -1
            count += (diff // x)
        return count