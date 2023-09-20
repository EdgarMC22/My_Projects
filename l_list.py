#linked list.py

from node import Node

class L_list:
	def __init__(self):
		self._front = None
		self._back = None
		self._length = 0

	def length(self):
		return self._length

	def insert(self, index, entry):
		new_node = Node(entry)
		if self._front == None:
			self._front = new_node
			self._back = new_node
			self._front.next = None
			self._back.next = None
			self._length += 1
		elif index > 0 and index < self._length:
			temp = self._front
			if temp.next == None:
				self._front.next = new_node
				self._back = new_node
				new_node.next = None
			else:
				counter = 1
				while counter < index:
					temp = temp.next
					counter += 1
				temp2 = temp.next
				temp.next = new_node
				new_node.next = temp2.next
				temp2 = new_node
			self._length += 1
		elif index == self._length:
				temp = self._front
				while temp.next != None:
					temp = temp.next
				temp.next = new_node
				self._back = new_node
				new_node.next = None
				self._length += 1

	def remove(self, index):
		if index >= 0 or index <= self._length - 1:
			if index == 0:
				self._front = self._front.next
				self._length -= 1
			else:
				counter = 1
				temp = self._front
				while counter < index:
					temp = temp.next
					counter += 1
				temp2 = temp.next
				temp2 = temp2.next
				temp.next = temp2
				self._length -= 1
		else:
			raise RuntimeError

	def get_entry(self, index):
		if index < self._length:
			temp = self._front
			counter = 0
			while counter < index:
				temp = temp.next
				counter += 1
			return temp.entry
		elif index == self._length:
			return self._back.entry
		else:
			raise RuntimeError

	def set_entry(self, index, entry):
		if index < self._length:
			new_node = Node(entry)
			temp = self._front
			counter = 1
			while counter < index:
				temp = temp.next
				counter += 1
			temp2 = temp.next
			temp.next = new_node
			new_node.next = temp2.next
			temp2 = new_node
		else:
			raise RuntimeError

	def clear(self):
		self._length = 0
		self._back = None
		self._front = None
