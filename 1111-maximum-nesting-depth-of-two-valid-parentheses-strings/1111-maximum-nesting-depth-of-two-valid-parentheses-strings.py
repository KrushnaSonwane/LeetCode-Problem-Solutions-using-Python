class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = list()
        for i, ch in enumerate(seq):
            if ch == "(":
                ans.append(i % 2)
            else:
                ans.append(1 - i % 2)
            # The above code can also be abbreviated to
            # ans.append((i & 1) ^ (ch == '('))
            # C++ and JavaScript code provide direct shorthand methods.
        return ans