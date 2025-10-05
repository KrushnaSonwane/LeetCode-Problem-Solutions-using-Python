class Solution:
    def pacificAtlantic(self, A: List[List[int]]) -> List[List[int]]:

        def solve(Q, visit):
            while Q:
                i, j = Q.pop()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < len(A) and 0 <= y < len(A[0]) and (x, y) not in visit and A[i][j] <= A[x][y]:
                        visit.add((x, y))
                        Q.append([x, y])
            return visit

        # above = set()
        visit = set()
        Q = []
        for i in range(len(A)):
            Q.append([i, 0])
            visit.add((i, 0))
        for i in range(len(A[0])):
            Q.append([0, i])
            visit.add((0, i))
        AA = solve(Q, visit)
        visit = set()
        Q = []
        for i in range(len(A)):
            Q.append([i, len(A[0])-1])
            visit.add((i, len(A[0])-1))
        for i in range(len(A[0])):
            Q.append([len(A)-1, i])
            visit.add((len(A)-1, i))
        BB = solve(Q, visit)
        res = []
        for a in AA:
            if a in BB:
                res.append(list(a))
        return res
        