class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        def help(num,rev):
            if num==0:
                return rev
            return help(num//10, rev*10 + (num%10)) 
        return x == help(x,0)       



           

        