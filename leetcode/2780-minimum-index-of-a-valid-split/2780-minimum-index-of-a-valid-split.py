class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        _map,left={},{} 
        for num in nums:
            _map[num]=_map.get(num,0) +1

        for i in range(len(nums)-1):
            left[nums[i]]=left.get(nums[i],0) +1
            _map[nums[i]] -=1


            if left[nums[i]] * 2 >(i +1) and _map[nums[i]] *2 > (len(nums)-i-1):
                return i
        return -1