'''
Name: Edgar Mendez
KUID: 3048729
Date Created: 09/26/2022
Last Modified: 09/26/2022
'''
#exercise1.py

def rec_power(i, base, temp, power):
	if power == 0:
		return 1
	elif power < 0:
		base = int(input("Enter a base: "))
		power = int(input("Enter a power: "))
		print("Sorry, your exponent must be zero or larger.")
		rec_power(0, base, power)
	elif power == 1:
		return base
	elif power == 2:
		return base*base
	elif i < power - 1:
		base = base*temp
		print(base)
		rec_power(i + 1, base, temp, power)




def main():
	base = int(input("Enter a base: "))
	power = int(input("Enter a power: "))
	if isinstance(base, int) == False or isinstance(power, int) == False or base == None or power == None:
		raise RuntimeError
	else:
		rec_power(0, base, base, power)

main()
