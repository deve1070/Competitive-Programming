class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # Helper function to perform fast exponentiation by squaring
        def fast_pow(x, n):
            if n == 0:
                return 1
            elif n < 0:
                x = 1 / x
                n = -n
            
            result = 1
            while n > 0:
                if n % 2 == 1:  # If n is odd
                    result *= x
                x *= x  # Square the base
                n //= 2  # Divide the exponent by 2
            
            return result
        
        return fast_pow(x, n)

