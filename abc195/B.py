A,B,W = map(int,input().split())
result = []
for a in range(A,B+1):
    if W*1000 % a == 0:
        result.append(int(W*1000 / a))
if result == []:
    print("UNSATISFIABLE")
else:
    print(min(result),max(result))

#公式解説#
# import math

# a,b,w=map(int,input().split())
# upper=int(math.floor(1000*w/a))
# lower=int(math.ceil(1000*w/b))

# if lower>upper:
#   print("UNSATISFIABLE")
# else:
#   print(lower,upper)
