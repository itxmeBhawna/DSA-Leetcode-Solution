class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        if far >= len(nums) - 1:
            return True
        for i in range(len(nums)):
            if i > far:
                return False
            far = max(far, i + nums[i])
        return True        
        