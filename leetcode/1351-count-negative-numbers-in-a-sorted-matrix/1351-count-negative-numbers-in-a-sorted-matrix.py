from collections import Counter
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #[[4,3,2,-1]
        #[3,2,1,-1]
        #[1,1,-1,-2]
        #[-1,-1,-2,-3]]
        combined=[]
        for g in grid:
            combined.extend(g)
        counter=Counter(combined)
        n_count=0
        for num in counter:
            if num < 0:
                n_count +=counter[num]
            else:
                continue
        return n_count
        