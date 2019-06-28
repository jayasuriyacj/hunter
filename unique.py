from collections import Counter
inp1=int(input())
inp2=list(map(int,input().split()))
inp3=Counter(inp2)
list=[]
for a in inp3.items():
  if(a[1] != 1):
    print(a[0],end = " ")
for b in inp3.items():
  list.append(b[1])
if(max(list) == 1):
  print("unique")
