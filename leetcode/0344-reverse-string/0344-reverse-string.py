class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.recursion(s,left=0,right=len(s)-1)
    
    def recursion(self,s,left,right):
        if left >= right:
            return
        s[left],s[right]=s[right],s[left]
        return self.recursion(s,left+1,right-1)
        
        