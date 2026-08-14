class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high - low)//2
            curr_load = 0
            day = 1
            for weight in weights:

                if curr_load + weight <= mid:
                    curr_load += weight
                else:
                    day +=1
                    curr_load = weight
            if day <= days:
                high = mid - 1
            else:
                low = mid +1
        return low                    

        