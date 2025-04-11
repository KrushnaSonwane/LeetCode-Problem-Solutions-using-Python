class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def check(num):
            # print(num, len(num))
            if len(num) % 2: return 0
            sum_ = 0
            for di in range(len(num)//2):
                sum_ += int(num[di])
            num = num[::-1]
            for di in range(len(num)//2):
                sum_ -= int(num[di])
            return sum_ == 0
        res = 0
        for i in range(low, high+1):
            res += check(str(i))
        return res