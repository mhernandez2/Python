m=int(raw_input("Ingrese m "))
n=int(raw_input("ingrese n "))
fn=1
f1=0
fm=1
f2=0
x=n-m
x1=0
xf=1
while x1<=x :
	x1+=1
	xf*=x1
while f1<=n :
	f1+=1
	fn*=f1
while f2<=m :
	f2+=1
	fm*=f2
c=fn/x*fm
print c
