class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_target(left,right,target):
            while left<right:
                mid = (left+right)//2
                if nums[mid]<target:
                    left = mid+1
                else:
                    right = mid
            return left if nums[left]==target else -1
        ## 先找旋轉點
        left,right = 0,len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<=nums[right]:
                right = mid
            else:
                left = mid+1
        
        ## 再從旋轉點切割成一半，每一半再做二分法
        min_index = left
        if nums[min_index]==target:
            return min_index
        a = find_target(0,min_index-1,target)
        b = find_target(min_index,len(nums)-1,target)
        return a if a>=0 else b