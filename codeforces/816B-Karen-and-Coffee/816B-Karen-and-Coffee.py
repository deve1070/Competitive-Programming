# B. Karen and Coffee
# Difference Array + Prefix Sum
# Time Complexity: O(n + MAX_TEMP + q)
# MAX_TEMP = 200000

import sys

input = sys.stdin.readline

n, k, q = map(int, input().split())

MAX_TEMP = 200000

# Difference array for range updates
diff = [0] * (MAX_TEMP + 2)

# Process recipes
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    if r + 1 <= MAX_TEMP:
        diff[r + 1] -= 1

# coverage[i] = number of recipes recommending temperature i
coverage = [0] * (MAX_TEMP + 1)

current = 0
for temp in range(1, MAX_TEMP + 1):
    current += diff[temp]
    coverage[temp] = current

# admissible[i] = 1 if temperature i is recommended by at least k recipes
admissible_prefix = [0] * (MAX_TEMP + 1)

for temp in range(1, MAX_TEMP + 1):
    admissible_prefix[temp] = admissible_prefix[temp - 1]
    if coverage[temp] >= k:
        admissible_prefix[temp] += 1

# Answer queries
for _ in range(q):
    a, b = map(int, input().split())
    print(admissible_prefix[b] - admissible_prefix[a - 1])