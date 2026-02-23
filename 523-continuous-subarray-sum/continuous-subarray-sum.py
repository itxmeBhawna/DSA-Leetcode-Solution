class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0:-1}
        pre_sum = 0
        for i in range (len(nums)):
            pre_sum += nums[i]
            if k!=0:
                remainder = pre_sum%k
            else:
                remainder = pre_sum
            if remainder in remainder_map:
                if i - remainder_map[remainder]>=2:
                    return True
            else:
                remainder_map[remainder]=i
        return False                       
        