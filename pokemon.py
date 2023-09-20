#pokemon.py
from bst import BST

class Pokemon:
	def __init__(self):
		self.lines = {}
		self.pokedex = BST()

	def read_file(self):
		temp = 1
		with open('sample.txt', 'r') as file:
			for line in file:
				self.lines[temp] = line.split()
				temp += 1

	def make_pokedex(self):
		self.read_file()
		temp = 1
		while temp < len(self.lines):
			temp_list = list(self.lines[temp])
			engl_name = str(temp_list[0])
			id = int(temp_list[1])
			jap_name= str(temp_list[2])
			self.pokedex.insert(id, engl_name, jap_name)
			temp += 1

	def search(self, id):
		if self.pokedex.is_in(id) == True:
			temp = 1
			while temp < len(self.lines):
				temp_list = list(self.lines[temp])
				if id == int(temp_list[1]):
					print(temp_list[0], temp_list[2], temp_list[1])
					temp = len(self.lines)
				else:
					temp += 1
		else:
			print("This Pokemon is not in the Pokedex")

	def print_preorder(self, root):
		if root:
			print(root.entry1, root.entry2, root.entry3)
			self.print_preorder(root.left)
			self.print_preorder(root.right)

	def print_postorder(self, root):
		if root:
			self.print_postorder(root.left)
			self.print_postorder(root.right)
			print(root.entry1, root.entry2, root.entry3)

	def add_pokemon(self, id, engl_name, jap_name):
		self.pokedex.insert(int(id), engl_name, jap_name)

	def print_menu(self):
		print("1) Search a pokemon by pokedex ID")
		print("2) Add a new pokemon to the pokedex")
		print("3) Print the pokedex")
		print("4) Quit")

	def run(self):
		self.make_pokedex()
		self.print_menu()
		choice = int(input("What do you want to do?(Enter a number): "))
		while choice != 4:
			if choice == 1:
				id = int(input("Enter a pokdex ID: "))
				self.search(id)
				self.print_menu()
				choice = int(input("What do you want to do?(Enter a number): "))
			if choice == 2:
				id = int(input("What us the pokedex ID for the new pokemon: "))
				engl_name = input("What is the English name for the new pokemon: ")
				jap_name = input("What is the Japanese name for the new pokemon: ")
				self.add_pokemon(id, engl_name, jap_name)
				self.print_menu()
				choice = int(input("What do you want to do?(Enter a number): "))
			if choice == 3:
				print("1) Print in Pre order")
				print("2) Print in order")
				print("3) Print in Post order")
				order = int(input("In what order do you want to print the pokedex?(Enter a number): "))
				if order == 1:
					self.print_preorder(self.pokedex.root)
				if order == 2:
					self.pokedex.print_in_order()
				if order == 3:
					self.print_postorder(self.pokedex.root)
				self.print_menu()
				choice = int(input("What do you want to do?(Enter a number): "))
		print("Exiting...")

