def max_sum(nums):
  _sum = max_s = 0
  for n in nums:
    _sum += n
    max_s = max(_sum , max_s)
  return max_s
    
t = int(input())
for _ in range(t):
  n = int(input())
  red = list(map(int,input().split()))
  m = int(input())
  blue = list(map(int,input().split()))
  print(max_sum(red)+max_sum(blue))