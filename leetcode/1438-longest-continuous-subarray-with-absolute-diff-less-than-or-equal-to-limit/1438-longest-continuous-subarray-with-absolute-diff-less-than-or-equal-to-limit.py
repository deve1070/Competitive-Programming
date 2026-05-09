# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Sliding Window + Monotonic Deques
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # max_deque keeps elements in decreasing order
        max_deque = deque()

        # min_deque keeps elements in increasing order
        min_deque = deque()

        left = 0
        best = 0

        for right in range(len(nums)):

            # Maintain decreasing max deque
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Maintain increasing min deque
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[right])

            # Shrink window if invalid
            while max_deque[0] - min_deque[0] > limit:

                # Remove left element if it leaves window
                if nums[left] == max_deque[0]:
                    max_deque.popleft()

                if nums[left] == min_deque[0]:
                    min_deque.popleft()

                left += 1

            # Update answer
            best = max(best, right - left + 1)

        return best