#pokedex.py
from bst import BST
from pokemon import Pokemon 

class Pokedex:
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
			name = str(temp_list[1])
			id = int(temp_list[0])
			hp_stat = int(temp_list[2])
			atk_stat = int(temp_list[3])
			def_stat = int(temp_list[4])
			spd_stat = int(temp_list[5])
			spec_stat = int(temp_list[6])	
			typing1 = str(temp_list[7])
			if len(temp_list) == 9:
				typing2 = str(temp_list[8])
				Pokemon.type2 = typing2
				self.pokedex.insert(id, name, hp_stat, atk_stat, def_stat, spd_stat, spec_stat, typing1, typing2)
			else:
 			    self.pokedex.insert(id, name, hp_stat, atk_stat, def_stat, spd_stat, spec_stat, typing1)   
			Pokemon.name = name 
			Pokemon.id = id
			Pokemon.hp = hp_stat
			Pokemon.atk = atk_stat
			Pokemon.defense = def_stat
			Pokemon.spd = spd_stat
			Pokemon.spec = spec_stat
			Pokemon.type1 = typing1
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