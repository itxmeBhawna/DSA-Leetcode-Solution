class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result =[]
        for num  in nums:
           
            result.append(num*num)
            ans = sorted(result)
        return ans    


        