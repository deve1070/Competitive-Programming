class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # nums[i] * (sum of spanning subarray)
        stack = []
        # mono increasing

        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        nums.append(float("-inf"))

        ans = 0

        for i , num in enumerate(nums):
            while stack and nums[stack[-1]] >= num:
                x = stack.pop()
                l = stack[-1] if stack else -1
                r = i
                _sum = pre[r] - pre[l + 1]
                # _sum = sum between r and l (both are exclusive)
                ans = max(ans, nums[x] * _sum)
            stack.append(i)
        return ans % (10 ** 9 + 7)