class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
       
        for i in range(len(str(low)), len(str(high))+1):
            for start in range(1, 10):
                last = start; num = 0
                for _ in range(i) :
                    num = num * 10 + last
                    last += 1
                    if last == 10: break
                if low <= num <= high and i == len(str(num)):
                    res.append(num)
        return res
