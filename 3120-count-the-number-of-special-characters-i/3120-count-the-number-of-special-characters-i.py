class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hashT, taken = set(), set()
        for ch in word:
            if ch.lower() == ch:
                if ch.upper() in hashT:
                    taken.add(ch)
            else:
                if ch.lower() in hashT:
                    taken.add(ch.lower())
            hashT.add(ch)
        return len(taken)