class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen ={}
       for i in range(len(nums)):

        value = nums[i]
        need = target - value
        if need in seen:
            return [seen[need],i] 
        seen[value] =i    

       
      
        



    
                      

                   
              
                    

        