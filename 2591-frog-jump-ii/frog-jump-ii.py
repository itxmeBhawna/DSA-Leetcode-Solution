class Solution:
    def maxJump(self, stones: list[int]) -> int:
        def possible(limit):
            for i in range(2, len(stones)):
                dist = stones[i] - stones[i-2]
                if dist > limit:
                    return False
            return True
        if len(stones) <= 2:
            return max(stones)    
        left = 0
        right = stones[-1] - stones[0]
        ans = 0
        while left <= right:
            mid  = left + (right - left)//2
            if possible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans            

        