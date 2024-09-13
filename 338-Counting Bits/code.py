class Solution:
    def countBits(self, n: int) -> List[int]:
        L = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            L[i] = L[i>>1]+(i%2)
        return L