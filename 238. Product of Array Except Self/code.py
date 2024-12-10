class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = nums[0]
        ans = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            ans[i]=left
            left=left*nums[i]
        right = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            ans[i]=right*ans[i]
            right*=nums[i]
        return ans
'''
    原始   [a1       ,a2    ,a3         ,a4]
    left   [ 1       ,a1    ,a1*a2      ,a1*a2*a3]
    right  [a2*a3*a4 ,a3*a4 ,a4         ,1]
'''