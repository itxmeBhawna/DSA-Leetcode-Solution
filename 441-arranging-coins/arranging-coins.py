class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        stair = 0
        while i<= n:
            n-=i
            stair +=1
            i+=1
        return stair    

            
