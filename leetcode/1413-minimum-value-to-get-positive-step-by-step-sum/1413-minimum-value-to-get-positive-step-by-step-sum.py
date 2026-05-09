class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_pref=float('inf')
        cur_sum=0

        for num in nums:
            cur_sum +=num
            min_pref=min(cur_sum,min_pref)
        if min_pref <=0:
            return abs(min_pref)+1
        else:
            return 1
        