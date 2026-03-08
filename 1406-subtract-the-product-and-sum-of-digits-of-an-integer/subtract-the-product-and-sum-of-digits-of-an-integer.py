class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_sum = 1
        digit_sum =0
        while n>0:
            digit = n%10
            product_sum *= digit
            
            digit_sum += digit
            n //=10
        return product_sum - digit_sum    



       
        