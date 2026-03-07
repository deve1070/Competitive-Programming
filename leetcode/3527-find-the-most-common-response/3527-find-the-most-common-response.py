class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        merged=[]
        for response in responses:
            merged.extend(list(set(response)))
        counter=Counter(merged)
        max_count=max(counter.values())
        #max_count=max(counter)
        

        most_common=min(response for response,count in counter.items() if count ==max_count)
        return most_common