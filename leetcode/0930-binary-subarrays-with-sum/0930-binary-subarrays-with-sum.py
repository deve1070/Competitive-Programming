# Number of Subarrays With Sum
# Prefix Sum + HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # prefix_count[prefix_sum] = how many times this prefix sum appeared
        prefix_count = defaultdict(int)
        prefix_count[0] = 1   # Empty prefix

        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num

            # If current_sum - goal existed before,
            # those prefixes form valid subarrays
            result += prefix_count[current_sum - goal]

            # Store current prefix sum
            prefix_count[current_sum] += 1

        return result