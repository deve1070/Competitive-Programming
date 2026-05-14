class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        count=0

        for pare in s:
            if pare=="(":
                stack.append(count)
                count =0
            else:
                count +=stack.pop() +max(count,1)
        return count

        # ans=0
        # for i in range(len(s)):
        #     if s[i]=="(":
        #         stack.append(s[i])
        #     else:
        #         stack.pop()
        #         if stack:
        #             ans *= len((stack))
        #         else:
        #             ans +=1

        return ans
        