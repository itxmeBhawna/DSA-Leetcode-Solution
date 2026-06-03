class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_no = 0
        max_no = max(nums)
        for i in range(min_no, max_no +1):
            if i not in nums:
                return i
        return max_no +1        



        