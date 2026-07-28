class Solution:
    def smallestPalindrome(self, S: str) -> str:
        hashT = Counter(S)
        A = sorted([[ch, hashT[ch]] for ch in hashT])
        print(A)
        res = []
        while A:
            ch, count = A.pop(0)
            res.append(ch * (count // 2))
        return ''.join(res) + ('' if len(S) % 2 == 0 else S[len(S) // 2]) + ''.join(res[::-1])