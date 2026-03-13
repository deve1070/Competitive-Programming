class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n ==0:
            return []
        stack=[]
        ans=[-1]*n
        for i in range(2*n-1,-1,-1):
            cur=nums[i%n]
            while stack and stack[-1] <= cur:
                stack.pop()
            if i < n:
                ans[i]=stack[-1] if stack else -1
            stack.append(cur)
        return ans             

        """
        nums=[1,2,1]
        stack=[]
        ans=[-1,-1,-1]

        stack=[1]
    1    ans=[-1,-1,-1]

    2   stack=[2]
        stack=[]
        ans=[2,-1,-1]


        stack=[2]


        """