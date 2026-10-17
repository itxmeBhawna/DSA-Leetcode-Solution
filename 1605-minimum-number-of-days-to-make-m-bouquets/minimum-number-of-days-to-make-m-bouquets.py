class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def helper(days):
            a = 0
            bouquets = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= days:
                    a+=1
                    if a == k:
                        bouquets += 1
                        a = 0
                else:
                    a = 0
                if bouquets == m:
                    return True
            return False

        low = min(bloomDay)
        high = max(bloomDay)
        ans = 0
        if len(bloomDay) < m*k:
            return -1
        while low <= high:
            mid = low + (high - low)// 2
            if helper(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans            

        