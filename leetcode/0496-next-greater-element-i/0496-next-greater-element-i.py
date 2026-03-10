class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res=[]
        # for i in range(len(nums1)):
        #     index=nums2.index(nums1[i])
        #     next_great=-1
        #     target_found=False
        #     for j in range(index +1,len(nums2)):
        #         if nums2[j] >nums1[i]:
        #             next_great=nums2[j]
        #             break
        #     res.append(next_great)
        # return res

        next_greater=defaultdict(lambda:-1)
        print(next_greater)
        stack=[]


        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()]=num
            stack.append(num)
        

        return [next_greater[num] for num in nums1]

