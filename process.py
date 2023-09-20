#process.py

from function import Function
from stack import Stack
from LQ import LQ

class Process:
	def __init__(self):
		self._lines = {}
		self._starts = {}
		self._calls = {}
		self._returns = {}
		self._raises = {}
		self.process = LQ()
		self.functStack = Stack()
		self._handlers = []
#reads the sample text and makes dictionaries of each line with their respective commands
	def read_file(self):
		temp = 1
		with open('sample.txt', 'r') as file:
			for line in file:
				self._lines[temp] = line.split()
				temp += 1
		temp = 1
		temp2 = 1
		temp3 = 1
		temp4 = 1
		temp5 = 1
		while temp <= len(self._lines):
			tempstr = str(self._lines[temp])
			if "START" in tempstr:
				self._starts[temp2] = self._lines[temp]
				temp2 += 1
			if "CALL" in tempstr:
				self._calls[temp3] = self._lines[temp]
				temp3 += 1
			if "RETURN" in tempstr:
				self._returns[temp4] = self._lines[temp]
				temp4 += 1
			if "RAISE" in tempstr:
				self._raises[temp5] = self._lines[temp]
				temp5 += 1
			temp += 1
#Using the dictionary that holds the lines of the text that gave a START command, each process name that followed was placed into the same dictionary with only the names
#Each process in the dictionary was then placed into a queue
	def create_processes(self):
		temp = 1
		while temp <= len(self._starts):
			tempstr = str(self._starts[temp]).split('START')
			tempstr = str(tempstr).replace("[", "")
			tempstr = str(tempstr).replace("]", "")
			tempstr = str(tempstr).replace('"', '')
			tempstr = str(tempstr).replace(",", "")
			tempstr = str(tempstr).replace("'", "")
			tempstr = str(tempstr).replace(" ", "")
			self._starts[temp] = tempstr
			self.process.enqueue(str(tempstr))
			temp += 1
			print(str(tempstr), "added to queue")
#Using the dictionary that holds the lines of the text that gave a CALL command, each function name was placed into a stack
#The handlers that followed the function names was placed into a list, the indexes were kept the same to keep track of which function a had which handler
	def create_functions(self):
		temp = 1
		while temp <= len(self._calls):
			handler = None
			tempstr = str(self._calls[temp]).split('CALL')
			tempstr = str(tempstr).replace("[", "")
			if "no" in str(tempstr):
				hanlder = False
				self._handlers.append("no")
			elif "yes" in str(tempstr):
				handler = True
				self._handlers.append("yes")
			tempstr = str(tempstr).replace("]", "")
			tempstr = str(tempstr).replace('"', '')
			tempstr = str(tempstr).replace(",", "")
			tempstr = str(tempstr).replace("'", "")
			tempstr = str(tempstr).replace(" ", "")
			self._calls[temp] = str(tempstr)
			if "no" in str(tempstr):
				tempstr = str(tempstr).replace("no", "")
			elif "yes" in str(tempstr):
				tempstr = str(tempstr).replace("yes", "")
			self._calls[temp] = str(tempstr)
			if handler ==  False:
				funct = Function(str(tempstr), "no")
			elif handler == True:
				funct = Function(str(tempstr), "yes")
			else:
				funct = Function(str(tempstr), None)
			self.functStack.push(funct)
			temp2 = temp
			if temp > len(self._starts):
				temp = len(self._starts)
				print(self._starts[temp], "calls", str(tempstr))
				temp = temp2
			else:
				print(self._starts[temp], "calls", str(tempstr))
			temp += 1
#Used If statements to check which process needs to be returned and dequeued and which functions need to be popped off the stack
	def returns(self):
		if len(self._returns) != 0:
			temp = len(self._starts)
			if temp > len(self._calls):
				print(self._starts[temp], "returns from main")
				print(self._starts[temp], "process has ended")
				self.process.dequeue()
			elif temp == len(self._calls):
				self.functStack.pop()
			elif temp < len(self._calls):
				self.functStack.pop()
				self.process.dequeue()
				self.process.enqueuq(self._starts[temp])
		else:
			pass
#Used a variety of If statements and while loops to check which function throws and exception and which functions handle the exceptions
	def raises(self):
		if len(self._raises) != 0:
			temp = 0
			temp2 = 1
			while temp < len(self._handlers):
				if self._handlers[temp] == "yes":
					for i in self._handlers:
						if i == "no":
							temp2 += 1
					print(self._starts[temp + 1], "encountered a raised by:", self._calls[temp2])
					while temp2 > 0:
						print(self._starts[temp + 1], "ends", self._calls[temp2], "due to unhandled exception")
						temp2 -= 1
					temp2 = 0
					while temp2 < len(self._handlers):
						if self._handlers[temp2] == "no":
							temp3 = temp2
							temp2 = len(self._handlers)
						else:
							temp2 += 1
					print(self._starts[temp + 1], "has exception handled by:", self._calls[temp3])
					self.functStack.pop()
				temp += 1
		else:
			pass

	def run(self):
		self.read_file()
		self.create_processes()
		self.create_functions()
		self.returns()
		self.raises()
