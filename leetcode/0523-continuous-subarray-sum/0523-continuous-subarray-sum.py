# Continuous Subarray Sum
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))

class Solution:
    def checkSubarraySum(self, nums, k):
        # remainder_map stores:
        # remainder -> first index where this remainder appeared
        remainder_map = {0: -1}

        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            # If same remainder seen before,
            # subarray sum between indices is divisible by k
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Store only first occurrence for longest distance
                remainder_map[remainder] = i

        return False