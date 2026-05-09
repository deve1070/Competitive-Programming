# C. New Year and Domino
# 2D Prefix Sum for horizontal + vertical domino placements
# Time Complexity:
# Preprocessing: O(h * w)
# Each Query: O(1)
# Total: O(h*w + q)

import sys

input = sys.stdin.readline

h, w = map(int, input().split())

grid = [input().strip() for _ in range(h)]

# horizontal[r][c]:
# number of horizontal dominoes ending at or before (r,c)
# horizontal domino starts at (r,c-1) and (r,c)
hor = [[0] * (w + 1) for _ in range(h + 1)]

# vertical[r][c]:
# number of vertical dominoes ending at or before (r,c)
ver = [[0] * (w + 1) for _ in range(h + 1)]

# Build prefix sums
for r in range(1, h + 1):
    for c in range(1, w + 1):

        # Carry previous prefix values
        hor[r][c] = hor[r - 1][c] + hor[r][c - 1] - hor[r - 1][c - 1]
        ver[r][c] = ver[r - 1][c] + ver[r][c - 1] - ver[r - 1][c - 1]

        # Horizontal domino check: current + left
        if c > 1 and grid[r - 1][c - 1] == '.' and grid[r - 1][c - 2] == '.':
            hor[r][c] += 1

        # Vertical domino check: current + above
        if r > 1 and grid[r - 1][c - 1] == '.' and grid[r - 2][c - 1] == '.':
            ver[r][c] += 1


def query(prefix, r1, c1, r2, c2):
    """Returns sum inside rectangle using 2D prefix"""
    return (
        prefix[r2][c2]
        - prefix[r1 - 1][c2]
        - prefix[r2][c1 - 1]
        + prefix[r1 - 1][c1 - 1]
    )


q = int(input().strip())

answers = []

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    # Horizontal dominoes must fit fully inside rectangle
    # so right cell can only go up to c2
    # left cell starts from c1+1 effectively
    horizontal_count = query(hor, r1, c1 + 1, r2, c2) if c1 < c2 else 0

    # Vertical dominoes must fit fully inside rectangle
    vertical_count = query(ver, r1 + 1, c1, r2, c2) if r1 < r2 else 0

    answers.append(str(horizontal_count + vertical_count))

sys.stdout.write("\n".join(answers) + "\n")