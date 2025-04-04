class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        arr = [0 for _ in range(n)]
        temp = []
        #### 製造一個遞減數列
        for i in range(n):
            while temp and temp[-1][0]<temperatures[i]:
                val,idx = temp.pop()
                arr[idx]=i-idx
            temp.append((temperatures[i],i))
        return arr