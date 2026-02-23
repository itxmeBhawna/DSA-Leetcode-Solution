class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left +(right - left)//2
            hours = 0
            for pile in piles:
                hours += ceil(pile/mid)
            if hours>h:
                left = mid +1
            else:
                right = mid
        return left                
        