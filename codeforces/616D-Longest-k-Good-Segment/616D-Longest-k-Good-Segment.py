import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=list(map(int,input().split()))

l=0
for r in range(k-1,n):
    seg=set(a[l:r])
    if len(seg) <=k:
        print(l+1,r+1)
        break
    else:
        l +=1
"""
# D. Longest k-Good Segment
# Sliding Window + Hash Map
# Time Complexity: O(n)
# Memory Complexity: O(k)

import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(int)

left = 0
distinct = 0

best_l = 0
best_r = 0

for right in range(n):
    # Add current element
    if count[a[right]] == 0:
        distinct += 1
    count[a[right]] += 1

    # Shrink window until it becomes k-good
    while distinct > k:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            distinct -= 1
        left += 1

    # Update best segment
    if right - left > best_r - best_l:
        best_l = left
        best_r = right

# Convert to 1-based indexing
print(best_l + 1, best_r + 1)