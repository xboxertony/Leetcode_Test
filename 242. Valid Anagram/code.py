class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for key in s:
            if key not in d:
                d[key]=1
            else:
                d[key]+=1
        for key in t:
            if key not in d or d[key]==0:
                return False
            d[key]-=1
            if d[key]==0:del d[key]
        
        return not d