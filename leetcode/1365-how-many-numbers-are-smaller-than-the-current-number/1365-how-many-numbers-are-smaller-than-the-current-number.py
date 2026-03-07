class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq=[0]*101
        for num in nums:
            freq[num] +=1
        
        for i in range(1,101):
            freq[i] +=freq[i-1]
        
        result=[0]*len(nums)
        for i,num in enumerate(nums):
            result[i]=freq[num -1] if num >0 else 0
        
        return result


