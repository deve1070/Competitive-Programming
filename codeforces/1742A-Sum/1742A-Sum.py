test_cases=int(input())
for _ in range(test_cases):
    a,b,c=map(int,input().split())

    if a==abs(c-b) or b==abs(a-c) or c==abs(a-b):
        print('YES')
    else:
         print("NO")