class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        # Initialize the current sum and max sum with the first element of the array
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update current_sum to either the current number or extend the subarray with the current number
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is larger
            max_sum = max(max_sum, current_sum)

        return max_sum

   