class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], val: List[int], k: int) -> int:
        hashT = defaultdict(list)
        inD = [0] * n
        if n == 1: return 1
        for a, b in edges:
            inD[a], inD[b] = inD[a] + 1, inD[b] + 1
            hashT[a].append(b)
            hashT[b].append(a)
        Q = []
        for i, node in enumerate(inD):
            if node == 1: 
                Q.append([i, val[i]])
                inD[i] -= 1
        res = 0
        while Q:
            node, sum_ = Q.pop(0)
            if val[node] % k == 0: res += 1
            for child in hashT[node]:
                inD[child] -= 1
                if sum_ % k != 0:
                    val[child] += sum_
                if inD[child] == 1:
                    Q.append([child, val[child]])
        return res
            