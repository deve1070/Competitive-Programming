class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most_k(nums,k)-self.at_most_k(nums,k-1)

    def at_most_k(self,nums,k):
        count=collections.Counter()
        ans=i=0
        for j in range(len(nums)):
            if count[nums[j]]==0:
                k -=1
            count[nums[j]] +=1
            while k <0:
                count[nums[i]] -=1
                if count[nums[i]]==0:k +=1
                i +=1
            ans +=j-i +1
        return ans

            
