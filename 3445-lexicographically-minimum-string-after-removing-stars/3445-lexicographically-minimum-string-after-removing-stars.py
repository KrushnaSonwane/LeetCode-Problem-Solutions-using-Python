class Solution:
    def clearStars(self, s: str) -> str:
        Q, visit = [], set()
        for i in range(len(s)):
            if s[i] == '*':
                visit.add(i)
                _, j = heappop(Q)
                visit.add(-j)
            else:
                heappush(Q, (s[i], -i))
        res = []
        for i in range(len(s)):
            if i not in visit:
                res.append(s[i])
        return ''.join(res)