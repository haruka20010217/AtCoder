N = int(input())
S = [list(map(int,input().split())) for i in range(N)]

temp = []

for a in range(N):
    time = 0.5
    for t in range(S[a][2] - 1):
        time = time + 1
    else:
        if time > S[a][0]:
            # print(time)
            temp.append(S[a][1])

# print(temp)

if temp == []:
    print("-1")
else:
    print(min(temp))


