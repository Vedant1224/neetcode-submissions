class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return n
        for i in range(n+1):
            if i*(i+1)/2 > n:
                return i-1
        