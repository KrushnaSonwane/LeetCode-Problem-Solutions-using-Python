class Solution:
    def minMaxDifference(self, num: int) -> int:
        A, B = [], []
        num = str(num)
        d1 = ''
        for d in num:
            if d == '9' or d1 == d: A.append('9'); continue
            if d1 == '' and d != '9':
                d1 = d; A.append('9')
            else:
                if d1==d:
                    A.append('9')
                else:
                    A.append(d)
        for d in num:
            if num[0] == d:
                B.append('0')
            else:
                B.append(d)
        print(A, B)
        return int(''.join(A)) - int(''.join(B))
