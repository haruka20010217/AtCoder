N,Y = map(int,input().split())
#連立方程式
for a in range(N+1):
    for b in range(N-a+1):
        c = N - a - b
        if 0 <= c <= 2000 and 10000*a + 5000*b + 1000*c == Y:
            print(a,b,c)
            exit()
print(-1,-1,-1)
