# B. Flip the Bits
# Codeforces solution
# Time Complexity: O(n) per test case

import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = input().strip()
    b = input().strip()

    # Find all positions where prefix has equal 0s and 1s
    balanced = [False] * n
    zeros = ones = 0

    for i in range(n):
        if a[i] == "0":
            zeros += 1
        else:
            ones += 1

        if zeros == ones:
            balanced[i] = True

    flipped = False
    possible = True

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        current = a[i]

        # If prefix has been flipped odd times, invert current bit logically
        if flipped:
            current = "1" if current == "0" else "0"

        # If current doesn't match target
        if current != b[i]:
            # We must flip prefix [0...i]
            if not balanced[i]:
                possible = False
                break
            flipped = not flipped

    print("YES" if possible else "NO")