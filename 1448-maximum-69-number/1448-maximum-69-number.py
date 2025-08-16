class Solution:
    def maximum69Number (self, num: int) -> int:
        res = [ch for ch in str(num)]
        for i, ch in enumerate(res):
            if ch == '6': res[i] = '9'; break
        return int(''.join(res))