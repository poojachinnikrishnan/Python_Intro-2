print("Enter the DNA string:")
s=input()
a=g=c=t=0
for i in s:
	if i=='A':
		a=a+1
	elif i=='G':
		g=g+1
	elif i=='C':
		c=c+1
	elif i=='T':
		t=t+1
print ('A='+str(a)+'\nG='+str(g)+'\nC='+str(c)+'\nT='+str(t))
