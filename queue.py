# queue.py

from node import Node

class LinkedQueue:
	def __init__(self):
		self._front = None
		self._back = None

	def enqueue(self, entry):
		new_node = Node(entry)
		if self._front == None:
			self._front = new_node
			self._back = new_node
			self._back.next = None
		elif self._front == self._back:
			self._front.next = new_node
			self._back = new_node
			self._back.next = None
		else:
			self._back = new_node

	def dequeue(self):
		if self._front != None:
			temp = self._front
			self._front = self._front.next
			return temp
		else:
			raise RunTimeError

	def peek_front(self):
		if self._front != None:
			return self._front
		else:
			raise RunTimeError

	def is_empty(self):
		if self._front == None and self._back == None:
			return True
		else:
			return False
