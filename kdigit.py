from itertools import combinations
x1,y1=input().split()
x=str(x1)
y=int(y1)
z=[]
a=combinations(x,len(x)-y)
for i in list(z):
    a.append(''.join(i))
print(min(a))
