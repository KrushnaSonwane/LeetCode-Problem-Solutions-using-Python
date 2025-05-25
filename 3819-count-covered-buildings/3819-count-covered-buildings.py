class Solution:
    def countCoveredBuildings(self, n: int, B: List[List[int]]) -> int:
        row, col = defaultdict(list), defaultdict(list)
        for x, y in B:
            row[x].append(y)
            col[y].append(x)
        for a in row:
            row[a].sort()
        for a in col:
            col[a].sort()
        res = 0
        for x, y in B:
            if len(row[x]) > 2 and row[x][0] != y and row[x][-1] != y and len(col[y]) > 2 and col[y][0] != x and col[y][-1] != x:
                res += 1
        return res