class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i =0
        j = len(nums)-1
        while i<=j:
            mid = i + (j -i)//2
            if nums[mid] == target:
                return mid
            elif nums[i]<target:
                i +=1
            elif nums[j] >target:
                j -=1
              
        return -1           

           
                
        