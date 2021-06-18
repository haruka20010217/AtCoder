N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
temp = []
for a in range(N):
    for b in range(N):
        if a == b:
            temp.append(A[a] + B[b])
        if a != b:
            if A[a] > B[b]:
                temp.append(A[a])    
            else:
                temp.append(B[b])
# print(temp)                
print(min(temp))
