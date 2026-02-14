class Solution:
    def champagneTower(self, poured: int, row: int, num: int) -> float:
        if row == 0: return min(poured, 1)
        res = [poured]
        for i in range(row):
            new_row = [0 for _ in range(len(res) + 1)]
            for j in range(0, len(new_row)-1):
                curr = res[j] - 1
                if curr > 0:
                    new_row[j] += curr / 2
                    new_row[j+1] += curr / 2
            res = new_row
        return min(res[num], 1)