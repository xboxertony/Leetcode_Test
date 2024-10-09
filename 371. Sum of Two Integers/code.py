class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # 32位整數的最大值，0111 1111 1111 ... 1111
        mask = 0xFFFFFFFF  # 32位mask，1111 1111 1111 ... 1111
        
        while b != 0:
            # 計算沒有進位的和
            sum_without_carry = (a ^ b) & mask
            # 計算進位
            carry = ((a & b) << 1) & mask
            # 更新a和b，繼續計算直到沒有進位
            a, b = sum_without_carry, carry
        
        # 如果a超過了最大正數範圍，代表是負數
        if a > MAX:
            a = ~(a ^ mask)
        return a
