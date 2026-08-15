class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = low + ( high - low)//2
            sub_arr = 1
            min_sum = 0
            for num in nums:
                if num + min_sum <= mid:
                    min_sum +=num
                else:
                    min_sum = num
                    sub_arr +=1
            if sub_arr <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low                        
        