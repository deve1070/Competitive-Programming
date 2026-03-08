class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=list(s.split(" "))
        patt_s={}
        s_patt={}
        if len(words) != len(pattern):
            return False
        for p,char in zip(pattern,words):
            if patt_s.get(p,0):
                if patt_s[p] !=char:
                    return False
                else:
                    patt_s[p]=char
            elif s_patt.get(char,0):
                if s_patt[char] !=char:
                    return False
                else:
                    s_patt[char]=p
            else:
                patt_s[p]=char
                s_patt[char]=p
        return True