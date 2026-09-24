class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(weights, days, cap):
            day = 1
            cur_load = 0
            for weight in weights:

                if cur_load + weight <= cap:
                    cur_load += weight
                else:
                    day += 1
                    cur_load = weight
            if day <= days:
                return True
            return False 

        left = max(weights)
        right = sum(weights)
        ans = 0
        while left <= right:
            mid = left + (right-left)//2
            if helper(weights, days, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid  + 1
        return ans            

            