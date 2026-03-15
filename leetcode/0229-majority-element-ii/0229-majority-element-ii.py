from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        freq=len(nums)//3
        result=[]
        for num in count:
            if count[num] >freq:
                result.append(num)
            else:
                continue
        return result
            
