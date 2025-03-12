class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            
            ### 我只留下高度嚴格遞增的序列
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                ### 假設把超出目前高度的長方形拿掉，必須留下他們所能圍成的面積
                max_area = max(max_area, height * (i - index))
                ### 這個 start 是紀錄目前該方形可以從 start 到 i 皆可圍成方形，因為移出的方形都比該方形高
                start = index
            
            stack.append((start, h))
        
        ### 最後開始統計從start到尾巴，可以圍成的最大方形，因為是遞增，所以可以保證圍的成功
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
            
        return max_area