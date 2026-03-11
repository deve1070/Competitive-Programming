class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if not nums or k == 0:
            return []

        deque_window = deque()  # This will store indices of elements in the window
        result = []

        for i in range(len(nums)):
            # Remove elements not within the current window
            if deque_window and deque_window[0] < i - k + 1:
                deque_window.popleft()

            # Remove elements that are smaller than the current element, as they will never be max
            while deque_window and nums[deque_window[-1]] < nums[i]:
                deque_window.pop()

            # Add current element index to the deque
            deque_window.append(i)

            # Add the max element (nums[deque_window[0]]) to result after the first k elements
            if i >= k - 1:
                result.append(nums[deque_window[0]])

        return result



