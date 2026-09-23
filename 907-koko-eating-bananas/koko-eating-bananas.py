class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1 
        right = max(piles)
        ans = 0
        

        while left <= right:
            mid = left + (right - left)//2
            hours = 0
            for pile in piles:
                hours += ceil(pile/mid)
            if hours <= h:
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans               
            


        