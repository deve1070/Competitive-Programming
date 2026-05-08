# Maximum Sum Obtained of Any Permutation
# Difference Array + Greedy Sorting
# Time Complexity: O(n log n + m)
# Space Complexity: O(n)

from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Count how many times each index is used
        diff = [0] * (n + 1)

        for start, end in requests:
            diff[start] += 1
            if end + 1 < n:
                diff[end + 1] -= 1

        # Step 2: Build frequency array using prefix sum
        freq = [0] * n
        current = 0

        for i in range(n):
            current += diff[i]
            freq[i] = current

        # Step 3: Assign largest nums to most requested positions
        nums.sort()
        freq.sort()

        # Step 4: Calculate maximum sum
        result = 0

        for num, count in zip(nums, freq):
            result = (result + num * count) % MOD

        return result