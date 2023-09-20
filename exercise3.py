'''
Name: Edgar Mendez
KUID: 3048729
Date Created: 09/30/2022
Last Modified: 09/30/2022
'''
#exercise3.py

class fib:
	def __init__(self):
		self.fib_list = [0, 1]

	def ith_fib(self, i, ith):
		if ith < 3:
			return self.fib_list[ith - 1]
		else:
			if i < ith:
				temp = self.fib_list[-1] + self.fib_list[-2]
				self.fib_list.append(temp)
				self.ith_fib(i + 1, ith)
			return self.fib_list[ith]

	def verify(self, check):
		temp = None
		self.ith_fib(0, check)
		for i in self.fib_list:
			if check == i:
				temp = True
			else:
				temp = False
		return temp



def main():
	f = fib()
	mode = input("Enter mode and value: ")
	if "-i" in mode:
		temp = str(mode.split("-i "))
		temp = temp.replace("[", "")
		temp = temp.replace("]", "")
		temp = temp.replace("'", "")
		temp = temp.replace(",", "")
		temp = temp.replace(" ", "")
		temp = int(temp)
		print(f.ith_fib(0, temp))
	elif "-v" in mode:
		temp = str(mode.split("-v "))
		temp = temp.replace("[", "")
		temp = temp.replace("]", "")
		temp = temp.replace("'", "")
		temp = temp.replace(",", "")
		temp = temp.replace(" ", "")
		temp = int(temp)
		if f.verify(temp) == True:
			print(temp, " is in the sequence")
		else:
			print(temp, "is not in the sequence") 
main()
