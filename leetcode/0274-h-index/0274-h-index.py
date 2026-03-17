class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        count=0

        for idx,val in enumerate(citations):
            """
            [0,1,3,5,6]
            0 ?= n-idx
            3= 5-(idx+1)

            [1,1,3]
            1=3-1
            """
            if val >= n-idx:
                count +=1
            else:
                continue
        return count
        