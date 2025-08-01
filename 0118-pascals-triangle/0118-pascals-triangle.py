class Solution:
    def generate(self, num: int) -> List[List[int]]:
        if num == 1: return [[1]]
        res = [[1]]
        for _ in range(num-1):
            tmp = [1]
            for i in range(len(res[-1])-1):
                tmp.append(res[-1][i] + res[-1][i+1])
            tmp.append(1)
            res.append(tmp)
        return res