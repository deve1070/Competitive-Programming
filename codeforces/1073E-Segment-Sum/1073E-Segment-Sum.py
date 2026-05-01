import sys

sys.setrecursionlimit(10**6)

MOD = 998244353

def digit_dp(s, k):
    # s is string representation of the number
    n = len(s)
    memo = {}

    def dp(pos, mask, tight, leading_zero):
        if pos == n:
            return (1 if not leading_zero else 0), 0   # count, sum

        key = (pos, mask, tight, leading_zero)
        if key in memo:
            return memo[key]

        ans_count = 0
        ans_sum = 0
        up = int(s[pos]) if tight else 9

        for d in range(0, up + 1):
            new_tight = tight and (d == up)
            new_leading = leading_zero and (d == 0)

            if new_leading:
                # Still all zeros
                new_mask = 0
                cnt, sm = dp(pos + 1, new_mask, new_tight, True)
                ans_count = (ans_count + cnt) % MOD
                ans_sum = (ans_sum + sm) % MOD
                continue

            # Not leading zero anymore
            new_mask = mask
            if d != 0 or not leading_zero:   # digit is actually used
                new_mask |= (1 << d)

            # Check if number of distinct digits exceeds k
            if bin(new_mask).count('1') > k:
                continue

            cnt, sm = dp(pos + 1, new_mask, new_tight, False)

            ans_count = (ans_count + cnt) % MOD

            # Contribution of this digit d * 10^(n-pos-1) * count_of_remaining
            power = pow(10, n - pos - 1, MOD)
            digit_contrib = (d * power % MOD) * cnt % MOD
            ans_sum = (ans_sum + digit_contrib + sm) % MOD

        memo[key] = (ans_count, ans_sum)
        return memo[key]

    return dp(0, 0, True, True)[1]   # return only the sum


def solve(l, r, k):
    def calc(x):
        if x < 0:
            return 0
        return digit_dp(str(x), k)

    res = (calc(r) - calc(l - 1) + MOD) % MOD
    return res


# Input
l, r, k = map(int, input().split())
print(solve(l, r, k))