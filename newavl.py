class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 0

class avl:		
	def __init__(self):
		self.root = None

	def insert(self,root,data):
		if self.root is None:
			self.root = node(data)
			return
		else:
			if data < root.data:
				if root.left is None:
					root.left = node(data)
					root.height = max(1,self.height(root.right)+1)
				else:
					self.insert(root.left,data)
					root.height = max(self.height(root.left),self.height(root.right))+1
					root.left = self.balance(root.left)
					root.height = max(self.height(root.left),self.height(root.right))+1
			else:
				if root.right is None:
					root.right = node(data)
					root.height = max(1,self.height(root.left)+1)
				else:
					self.insert(root.right,data)
					root.height = max(self.height(root.left),self.height(root.right))+1
					root.right = self.balance(root.right)
					root.height = max(self.height(root.left),self.height(root.right))+1

	def delete(self,root,data):
		if data < root.data:
			root.left = self.delete(root.left,data)
		elif data > root.data:
			root.right = self.delete(root.right,data)
		else:
			if(root.left is None and root.right is None):
				root = None
				return root
			elif root.left is None:
				root = root.right
			elif root.right is None:
				root = root.left
			else:
				temp = self.findmin(root.right)
				root.data = temp.data
				root.right = self.delete(root.right,temp.data)
		root.height = max(self.height(root.left),self.height(root.right))+1
		root = self.balance(root)
		root.height = max(self.height(root.left),self.height(root.right))+1
		return root	  
					
			
		
	def height(self,temp):
		if temp is None:
			return -1
		else:
			return temp.height

	def balance(self,temp):
		if self.diff(temp)==2:
			if self.diff(temp.left)==-1:
				temp = self.rightleftrotate(temp)
			else:	
				temp = self.rightrotate(temp)
		elif self.diff(temp)==-2:
			if self.diff(temp.right)==1:
				temp = self.leftrightrotate(temp)
			else:
				temp = self.leftrotate(temp)
		return temp

	def diff(self,temp):
		return(self.height(temp.left)-self.height(temp.right))

	def leftrotate(self,temp):
		temp1 = temp.right
		temp.right = temp1.left
		temp1.left = temp	
		temp.height = max(self.height(temp.left),self.height(temp.right))+1
		temp1.height = max(self.height(temp1.left),self.height(temp1.right))+1
		return temp1

	def rightrotate(self,temp):
		temp1 = temp.left
		temp.left = temp1.right
		temp1.right = temp
		temp.height = max(self.height(temp.left),self.height(temp.right))+1
		temp1.height = max(self.height(temp1.left),self.height(temp1.right))+1
		return temp1

	def rightleftrotate(self,temp):
		temp.left = self.leftrotate(temp.left)
		temp = self.rightrotate(temp)
		return temp

	def leftrightrotate(self,temp):
		temp.right = self.rightrotate(temp.right)
		temp = self.leftrotate(temp)
		return temp

	def preorder(self,temp):
		if temp is None:
			return
		else:
			print(temp.data)
			self.preorder(temp.left)
			self.preorder(temp.right)

tree = avl()
tree.insert(tree.root,14)
tree.insert(tree.root,17)
tree.insert(tree.root,11)
tree.insert(tree.root,7)
tree.insert(tree.root,53)
tree.insert(tree.root,4)
tree.insert(tree.root,13)
tree.insert(tree.root,12)
tree.insert(tree.root,8)
tree.root = tree.delete(tree.root,53)
tree.preorder(tree.root)