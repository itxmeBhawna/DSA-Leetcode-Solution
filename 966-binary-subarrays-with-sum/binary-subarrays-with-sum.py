class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {0:1}
        cur_sum = 0
        count= 0
        for num in nums:
            cur_sum += num
            if cur_sum - goal in seen:
                count += seen[cur_sum-goal]
            seen[cur_sum] = seen.get(cur_sum, 0)+1
        return count
        