n,a,d=map(int,input().split())
s=0
for i in range(0,n-1):
  s=s+a
  a=a+d
print(s)
