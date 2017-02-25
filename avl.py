class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1 

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
				else:	
					self.insert(root.left,data)
					self.height(root.left)
					root.left = self.balance(root.left)

			else:
				if root.right is None:		
					root.right = node(data)
				else:
					self.insert(root.right,data)	
					self.height(root.right)
					root.right = self.balance(root.right)
		self.height(self.root)	
		self.balance(self.root)		

	def delete(self,root,data):
		if root is None:
			return root
		elif data < root.data:
			root.left = self.delete(root.left,data)
		elif data > root.data:
			root.right = self.delete(root.right,data)
		else:
			if(root.left is None and root.right is None):
				root = None
			elif root.left is None:
				root = root.right
			elif root.right is None:
				root = root.left
			else:
				temp = self.findmin(root.right)
				root.data = temp.data
				root.right = self.delete(root.right,temp.data)
		self.height(root)
		root = self.balance(root)
		return root	    


	def findmin(self,root):
		while(root.left):
			root = root.left
		return root


	def height(self,temp):
		if temp is None:
			return 
		if (temp.left is None and temp.right is None):
			temp.height = 1
		elif temp.left is None:
			temp.height = temp.right.height+1
		elif temp.right is None:
			temp.height = temp.left.height+1
		else:
			if temp.left.height > temp.right.height:
				temp.height = temp.left.height+1
			else:
				temp.height	= temp.right.height+1

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

	def leftrotate(self,temp):
		temp1 = temp.right
		temp.right = temp1.left
		temp1.left = temp	
		self.height(temp)
		self.height(temp1)
		return temp1

	def rightrotate(self,temp):
		temp1 = temp.left
		temp.left = temp1.right
		temp1.right = temp
		self.height(temp)
		self.height(temp1)
		return temp1

	def rightleftrotate(self,temp):
		temp.left = self.leftrotate(temp.left)
		temp = self.rightrotate(temp)
		return temp

	def leftrightrotate(self,temp):
		temp.right = self.rightrotate(temp.right)
		temp = self.leftrotate(temp)	
		return temp

	def diff(self,temp):
		if temp is None:
			return 0
		elif (temp.left is None and temp.right is None):
			return 0
		elif temp.left is None:
			return 0-temp.right.height
		elif temp.right is None:
			return temp.left.height	
		return temp.left.height-temp.right.height

	def preorder(self,temp):
		if temp is None:
			return
		else:
			print(temp.data)
			print(temp.height)
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