class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = ceil(n/2)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            coin_need = ceil(mid*(mid + 1)/2)
            if coin_need <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans            
        

            
