class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        for i in range(len(height)-1):
            left.append(max(height[i],left[-1]))
        s = 0
        right = 0
        for j in range(len(height)-1,-1,-1):
            s+=max(min(left[j],right)-height[j],0)
            '''
            要取大於0的數字，因為可能會發生 
            left 是3，right 是0
            這種狀況，兩邊取小是0，減去當下階梯高度就變成負值
            '''
            right = max(right,height[j])
        return s