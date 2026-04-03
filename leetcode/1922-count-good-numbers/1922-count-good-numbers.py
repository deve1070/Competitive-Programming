class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9 +7

        def power_mod(a,b,m):
            if b==0:
                return 1
            half=power_mod(a,b//2,m)
            if b%2==0:
                return (half*half)%m
            else:
                return (half*half*a)%m
        even=(n+1)//2
        odd=n//2

        return (power_mod(5,even,MOD)*power_mod(4,odd,MOD))%MOD
