matrix=[list(map(int,input().split())) for _ in range(5)]
index=0
for i in range(5):
    if 1 in matrix[i]:
        index=(i,matrix[i].index(1))
    else:
        continue
print(abs(index[0]-3 +1) + abs(index[1] +1 -3))