class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        ### 由於題目有說每個數字在-10000~10000之間，所以可以利用桶排序的想法，為每個數字建桶

        array = [0] * (20001)

        for i in nums:

            array[i + 10000] += 1

        for i in range(20000, -1, -1):

            k -= array[i]

            if k <= 0:

                return i - 10000
