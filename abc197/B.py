H,W,X,Y = map(int,input().split())
S = []
for a in range(H):
  t_s = input()
  S.append(t_s)

#2次元配列標準入力
#  [[int(S) for s in input().split("")] for i in range (N)]

count = 0

print(S)
print(S[0][1])

for a in range(X,H):
    if (S[a][Y-1] != '#'):
        count = count + 1
    else:
        break
print(count)

for a in range(X, 0, -1):
    if (S[a][Y-1] != '#'):
        count = count + 1
    else:
        break

for b in range(Y,W):
    if (S[X-1][b] != '#'):
        count = count + 1
    else:
        break

for b in range(Y,0,-1):
    if (S[X-1][b] != '#'):
        count = count + 1
    else:
        break
# for a in range(X,0):
#     if S[X-1][a] != '#':
#         count = count + 1
#     else S[X-1][a] == '#':
#         break

# for b in range(Y,W):
#     if S[b][Y-1] != '#':
#         count = count + 1
#     else S[b][Y-1] == '#':
#         break

# for b in range(Y,0):
#     if S[b][Y-1] != '#':
#         count = count + 1
#     else S[b][Y-1] == '#':
#         break




print(count-1)