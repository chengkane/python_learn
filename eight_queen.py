#!/usr/bin/python
# eight queens problems*/

result=[]
used=[]
unused=set(range(1,9))
diag=set()

def find():
	if len(used)==8:
		if len(result)<100:
			result.append(tuple(used))
	else:
		temp=tuple(unused)
		for a in temp:
			m=a+len(used)
			n=a-len(used)-8
			if m not in diag and n not in diag:
				used.append(a)
				unused.remove(a)
				diag.add(m)
				diag.add(n)
				find()
				diag.remove(m)
				diag.remove(n)
				used.pop()
				unused.add(a)

find()

for i in range(len(result)):
	print '%2d'%(i+1),result[i]

