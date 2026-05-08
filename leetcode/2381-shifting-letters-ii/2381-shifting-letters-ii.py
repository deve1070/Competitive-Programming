class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        diff=[0] *(n+1)
        for start,end,dirc in shifts:
            if dirc ==1:
                diff[start] +=1
                if end +1 <n:
                    diff[end+1] -=1
            else:
                diff[start] -=1
                if end +1 < n:
                    diff[end+1] +=1
        result=[]
        shift=0
        for i in range(n):
            shift +=diff[i]
            new_char=(ord(s[i])-ord('a') +shift) %26

            result.append(chr(new_char +ord('a')))
        
        return "".join(result)
        