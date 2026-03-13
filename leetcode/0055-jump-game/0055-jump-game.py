class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for curr in range(len(nums)):
            if curr > far:
                return False
            far = max(far, curr + nums[curr])
        return True