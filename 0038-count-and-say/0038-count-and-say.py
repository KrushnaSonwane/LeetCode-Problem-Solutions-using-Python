class Solution(object):
    def countAndSay(self, n):
        if n == 1: return '1'
        ans = '1'
        for i in range(1, n):
            count, currStr, nextAns = 1, ans[0], ''
            for j in range(1, len(ans)):
                if currStr == ans[j]:
                    count += 1
                else:
                    nextAns += (str(count) + currStr)
                    currStr, count = ans[j], 1
            nextAns += (str(count) + currStr)
            ans = nextAns
        return ans
    
        #With Separate Helper Function
        def countStr(n):
            temp, c = n[0], 1
            l = []
            for i in range(1, len(n)):
                if n[i] == temp: c += 1
                else:
                    l.append([str(c), temp])
                    c = 1
                    temp = n[i]
            l.append([str(c), temp])
            return combine(l)
            
        def combine(l):
            ans = ''
            for i in range(len(l)):
                ans += (l[i][0] + l[i][1])
            return ans
        
        if n == 1: return '1'
        ans = '1'
        for i in range(1, n):
            ans = countStr(ans)
        return ans
    
        #Without Helper Function
        if n == 1: return '1'
        ans = '1'
        for i in range(1, n):
            countList, count, currStr = [], 1, ans[0]
            for j in range(1, len(ans)):
                if currStr == ans[j]:
                    count += 1
                else:
                    countList.append([str(count), currStr])
                    currStr, count = ans[j], 1
            countList.append([str(count), currStr])
            ans = ''
            for i in range(len(countList)):
                ans += (countList[i][0] + countList[i][1])
        return ans