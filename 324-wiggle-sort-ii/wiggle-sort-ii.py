class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = [0]*len(nums)
        n = len(nums)
        nums.sort()
        mid = (n-1) // 2
        high = n-1
        for i in range(0,n,2):
            ans[i] = nums[mid]
            mid -=1
        for i in range(1, n, 2):
            ans[i] = nums[high]
            high -=1
        nums[:] = ans        
        
        