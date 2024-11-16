class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx,key in enumerate(nums):
            if key in d:
                return [d[key],idx]
            d[target-key]=idx