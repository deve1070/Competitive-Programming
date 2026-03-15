class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq=Counter(s)
        res=[]

        for char in order:
            if char in s:
                res.append(char*freq[char])
        res.extend([char for char in s if char not in order])

        return "".join(res)