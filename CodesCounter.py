
import os

filetype=set(['c','cpp','h',
			'html','css','js',
			'java',
			'py',
			'bat','sh'])
def count(path,layer=5):
	if layer==0:
		return None
	try:
		filelist=os.listdir(path)
	except BaseException:
		return None
	doc=filter(lambda x: os.path.isfile(os.path.join(path,x)) and os.path.splitext(x)[-1][1:] in filetype and o,filelist)
	dire=filter(lambda x: os.path.isdir(os.path.join(path,x)) and x[0] not in '.$',filelist)
	sum=0
	txt,err,childdir=[],[],[]
	result=[0,path+os.sep,txt,err,childdir]
	for x in doc:
		try:
			temp=open(os.path.join(path,x))
		except IOError:
			err.append('Can\'t open '+x)
		else:
			n=temp.read().count('\n')
			temp.close()
			sum+=n
			txt.append('%3d %s'%(n,x))
	for x in dire:
		temp=count(os.path.join(path,x),layer-1)
		if temp:
			sum+=temp[0]
			childdir.append(temp)
	result[0]=sum
	return result

def count_print(arg):
	if arg and sum(map(len,arg[2:]))>0:
		print '%4d in %s'%(arg[0],arg[1])
		temp=''
		for x in arg[2]:
			temp+=x+' '*(20-len(x)%20)
		if len(temp)>0:
			print temp[:-1]
		temp=''
		for x in arg[3]:
			temp+=x+' '*(20-len(x)%20)
		if len(temp)>0:
			print temp[:-1]
		for x in arg[4]:
			count_print(x)

a=count('.')
count_print(a)
raw_input('press enter to exit...')

