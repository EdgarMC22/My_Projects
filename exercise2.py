'''
Name: Edgar Mendez
KUID: 3048729
Date Created: 09/26/2022
Last Modified: 09/29/2022
'''
#exercise2.py

class sick:
	def __init__(self):
		self.sick_list = [6, 20, 75]

	def outbreak(self, i, days):
		if days < 4:
			return self.sick_list[days - 1]
		else:
			if i < days:
				temp = self.sick_list[-1] + self.sick_list[-2] + self.sick_list[-3]
				self.sick_list.append(temp)
				self.outbreak(i + 1, days)
			return self.sick_list[days - 1]

def main():
	s = sick()
	print("OUTBREAK!")
	days = int(input("What day do you want a sick count for?: "))
	if days <= 0:
		print("Invalid day")
		days = int(input("What day do you want a sick count for?: "))
	print(s.outbreak(0, days))
main()
