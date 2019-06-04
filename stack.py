class Node():
	def __init__(self, *args):
		if len(args)==0:
			self.data = None
			self.next = None
		elif len(args)== 1:
			self.data = args[0]
			self.next = None
			print(args)

	def __str__(self):
		return "{}".format(self.data)
class Stack():
	def __init__(self, *args):
		if len(args)==0:
			self.data = None
			self.num = 0
			self.root = None
		elif len(args)== 1:
			self.root = Node(args[0])
			self.num = 1
	def push (self, data):
		new = Node(data)
		new.next= self.root
		self.num = self.num +1
		self.root = new


	def pop(self):
		data = self.root.data
		temp = self.root
		self.root = self.root.next
		temp = None	
		return data

	def  __str__(self):
		texto = ""
		nodo = self.root
		while nodo:
			texto = texto +str(nodo.data)+ "\n"
			nodo = nodo.next
		return texto