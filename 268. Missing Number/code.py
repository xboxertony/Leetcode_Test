class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a^=i
        for j in range(0,len(nums)+1):
            a^=j
        
        return a