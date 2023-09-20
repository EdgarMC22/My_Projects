#Binary Search Tree
from node import Node

class BST:
	def __init__(self):
		self.root = None

	def insert(self, entry1, entry2, entry3):
		new_node = Node(entry1, entry2, entry3)
		if self.root == None:
			self.root = new_node
			return
		prev = None
		temp = self.root
		while temp != None:
			if temp.entry1 > new_node.entry1:
				prev = temp
				temp = temp.left
			elif temp.entry1 < new_node.entry1:
				prev = temp
				temp = temp.right
		if prev.entry1 > new_node.entry1:
			if prev.entry1 != new_node.entry1:
				prev.left = new_node
			else:
				raise RuntimeError
		else:
			if prev.entry1 != new_node.entry1:
				prev.right = new_node
			else:
				raise RuntimeError

	def is_in(self, id):
		temp = self.root
		if id == int(temp.entry1):
			return True
		else:
			if id > int(temp.entry1):
				temp = temp.right
			elif id < int(temp.entry1):
				temp = temp.left
			if id != int(temp.entry1):
				while int(temp.entry1) != id:
					if id > int(temp.entry1):
						if temp.right != None:
							if id == int(temp.entry1):
								return True
							else:
								temp = temp.right
						else:
							return False
					elif id < int(temp.entry1):
						if temp.right != None:
							if id == int(temp.entry1):
								return True
							else:
								temp = temp.left
						else:
							return False
				return True
			else:
				return True

	def print_in_order(self):
		temp = self.root
		temp_list = []
		while temp != None or not len(temp_list) == 0:
			if temp != None:
				temp_list.append(temp)
				temp = temp.left
			else:
				temp = temp_list.pop()
				print(temp.entry1, temp.entry2, temp.entry3)
				temp = temp.right


