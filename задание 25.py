a=list(map(int,input().split()))
r=a[0]*a[2]+a[1]*a[2]//100
k=a[1]*a[2]%100
print(r,'руб.',k,'коп.')