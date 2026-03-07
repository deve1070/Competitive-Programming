class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compar(a,b):
            if str(a) +str(b) >str(b) +str(a):
                return -1
            return 1

        sorted_nums = sorted(nums,key=cmp_to_key(compar))
        if sorted_nums[0]==0:
            return "0"

        print(sorted_nums)
        return "".join(str(num) for num in sorted_nums)
