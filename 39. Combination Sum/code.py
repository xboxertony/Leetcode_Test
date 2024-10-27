class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = []
        ans = []
        def backtracking(nums,index):
            if sum(nums)>target:
                return
            if sum(nums)==target:
                ans.append(nums[:])
                return
            for i in range(index,len(candidates)):
                nums.append(candidates[i])
                backtracking(nums,i)
                nums.pop()
        backtracking(nums,0)
        return ans