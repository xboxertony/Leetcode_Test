class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        m = 0
        for i in d:
            if i-1 not in d:
                v = 1
                j = i
                while j+1 in d:
                    v+=1
                    j+=1
                m = max(m,v)
        return m