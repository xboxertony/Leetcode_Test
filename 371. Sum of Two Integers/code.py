class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF  # 32位整數的最大值，0111 1111 1111 ... 1111
        mask = 0xFFFFFFFF  # 32位mask，1111 1111 1111 ... 1111
        print(f"a = {a:032b}, b = {b:032b}")
        
        while b != 0:
            # 計算沒有進位的和
            sum_without_carry = (a ^ b) & mask
            # 計算進位
            carry = ((a & b) << 1) & mask
            # 更新a和b，繼續計算直到沒有進位
            a, b = sum_without_carry, carry
            print(f"a = {a:032b}, b = {b:032b}")
        
        # 如果a超過了最大正數範圍，代表是負數
        if a > MAX:
            print("a^mask",f'{(a ^ mask):032b}')
            a = ~(a ^ mask)
            print("final",f'{a:032b}')
        '''
        如果 a 超過了最大正數範圍，代表它應該是負數。
        以 -2 舉個例子
        在一般程式語言中，-2 的 32 位元表示為 0xFFFFFFFE。
        但是，在 Python 中，因為整數可以到 64 位元，-2 會表示為 0x00000000FFFFFFFE，
        這樣的表示會被當作正數，因為在 64 位元中，最前面的位元是 0（表示正數）。
        因此，我們需要對後面的 32 位元取反（a ^ mask），之後再取一次反（~），
        這樣才能確保前 32 位元都變成 1，得到正確的二補數表示。
        最終，-2 將被表示為 0xFFFFFFFFFFFFFFFE。
        '''
        return a