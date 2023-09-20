#stack.py

from node import Node

class Stack:
	def __init__(self):
		self._top = None

	def push(self, entry):
		new_node = Node(entry)
		if self._top == None:
			new_node.next = self._top
		self._top = new_node

	def pop(self):
		if self._top != None:
			temp = self._top.entry
			self._top = self._top.next
			return temp
		else:
			raise RuntimeError

	def peek(self):
		if self._top != None:
			return self._top
		else:
			raise RuntimeError

	def is_empty(self):
		if self._top == None:
			return True
		else:
			return False
