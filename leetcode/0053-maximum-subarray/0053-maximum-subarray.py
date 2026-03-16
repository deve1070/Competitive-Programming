class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #[-2,-1,-4,0,-1,1,2,-3,1]
        # 2-(-4) -0 0=6
        # 1-(-2) +-2=1
        # -3 +2 -2=-3 
        current_sum = nums[0]
        best_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            best_sum = max(best_sum, current_sum)

        return best_sum