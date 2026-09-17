a=list(map(int,input().split()))
x=a[0]
y=a[1]
print(int(x%y==0 or y%x==0))