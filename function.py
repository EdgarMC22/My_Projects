#function.py

from node import Node

class Function:
	def __init__(self, name, handler):
		self._name = Node(name)
		self._handler = None
