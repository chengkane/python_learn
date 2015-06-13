
class pack(object):
	def __init__(self,volume):
		self.items=[]
		self.room=self.value=0
		self.volume=volume
	def add(self,item):
		if self.room+item[0] > self.volume:
			return False
		self.items.append(item)
		self.room+=item[0]
		self.value+=item[1]
		return True
	def pop(self):
		temp=self.items.pop()
		self.room-=temp[0]
		self.value-=temp[1]
		return temp
	def isempty(self):
		return len(self.items)==0
	def copy(self):
		result=pack(self.volume)
		result.items=self.items[:]
		result.room,result.value=self.room,self.value
		return result
	def __str__(self):
		return '%s\nvalue:%d  room:%d  volume:%d\n'%(str(self.items),self.value,self.room,self.volume)

def package(sofar,todo,result):
	if todo.isempty():
		if len(result)==0 or sofar.value==result[-1].value:
			result.append(sofar.copy())
		elif sofar.value>result[-1].value:
			while len(result)>0:
				result.pop()
			result.append(sofar.copy())
	else:
		if len(result)==0 or sofar.value+todo.value>result[-1].value:
			temp=todo.pop()
			package(sofar,todo,result)
			if sofar.add(temp):
				package(sofar,todo,result)
				sofar.pop()
			todo.add(temp)

result=[]
todo=pack(1000)
items=[(1,2),(3,4),(4,5),(5,6),(7,8)]
for x in items:
	todo.add(x)
sofar=pack(10)
package(sofar,todo,result)
for x in result:
	print x
