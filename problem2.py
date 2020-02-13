print('ENTER THE DNA SEQUENCE')
s=input()
rna=''
for i in s:
	if i=='T':
	 rna=rna+'U'
	else:
	 rna= rna+i
print(rna)
 
