import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = list(map(int, input().split()))

    # L[i] = sum of min(m[j]..m[i]) for j=0..i  (treating i as peak, left side)
    # R[i] = sum of min(m[i]..m[j]) for j=i..n-1 (treating i as peak, right side)
    L = [0] * n
    R = [0] * n

    # Monotonic stack: list of [value, count]
    # Compute L left to right
    stack = []  # [value, count]
    cur_sum = 0
    for i in range(n):
        val = m[i]
        cnt = 1
        while stack and stack[-1][0] >= val:
            v, c = stack.pop()
            cur_sum -= v * c
            cur_sum += val * c
            cnt += c
        stack.append([val, cnt])
        cur_sum += val
        L[i] = cur_sum

    # Compute R right to left
    stack = []
    cur_sum = 0
    for i in range(n - 1, -1, -1):
        val = m[i]
        cnt = 1
        while stack and stack[-1][0] >= val:
            v, c = stack.pop()
            cur_sum -= v * c
            cur_sum += val * c
            cnt += c
        stack.append([val, cnt])
        cur_sum += val
        R[i] = cur_sum

    # Find best peak
    best = max(range(n), key=lambda i: L[i] + R[i] - m[i])

    # Reconstruct answer
    a = [0] * n
    cur_min = m[best]
    for i in range(best, -1, -1):
        cur_min = min(cur_min, m[i])
        a[i] = cur_min
    cur_min = m[best]
    for i in range(best, n):
        cur_min = min(cur_min, m[i])
        a[i] = cur_min

    sys.stdout.write(' '.join(map(str, a)) + '\n')

solve()