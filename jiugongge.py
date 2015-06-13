

def judge(a,b,c,d):
	a,b=abs(a-c),abs(b-d)
	c=a+b
	if c==4 or c==2 and (a==0 or b==0):
		return False
	return True

def inte(x,y):
	return ((x[0]+y[0])/2,(x[1]+y[1])/2)

def find(done,todo,result,n):
	temp=list(todo)
	for x in todo:
		if judge(done[-1][0],done[-1][1],x[0],x[1]) or inte(done[-1],x) in done:
			temp.remove(x)
			done.append(x)
			find(done,temp,result,n)
			temp.append(done.pop())
			if(len(done)>=3):
				result[len(done)]+=n
	return result

if __name__=='__main__':
	import time
	start=time.clock()
	todo=[ (x,y) for x in range(1,4) for y in range(1,4) ]
	#result=0
	result=[0]*9
	test=[ (1,1) , (1,2) , (2,2) ]
	valu=[4,4,1]
	for x,y in zip(test,valu):
		todo.remove(x)
		find([x],todo,result,y)
		todo.append(x)
	print(result)
	print('sum:',sum(result))
	start=time.clock()-start
	print('time:',start,'s')


