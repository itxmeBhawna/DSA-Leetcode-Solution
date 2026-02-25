class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {0:1}
        add = 0
        count= 0
        for num in nums:
            add += num
            if add - goal in seen:
                count += seen[add-goal]
            seen[add] = seen.get(add, 0)+1
        return count
        