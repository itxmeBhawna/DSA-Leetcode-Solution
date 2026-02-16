class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        in_pos =0
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[in_pos] = nums[i]
                in_pos +=1
        for i in range(in_pos,len(nums)):
            nums[i] = 0

