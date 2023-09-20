'''
Name: Edgar Mendez
KUID: 3048729
Date: 10/22/21
Lab: 06
Last modified: 10/22/21
Purpose: Digit Functions
'''

def last_digit(num):
	num_list = list(str(num))
	return num_list[-1]

def remove_last_digit(num):
	num_list = list(str(num))
	if len(num_list) <= 1:
		return 0
	else:
		num_list2 = num_list[:-1]
		return num_list2

def add_digit(current_num, new_digit):
	num_list = list(str(current_num))
	num_list[len(num_list):] = str(new_digit)
	return num_list

def reverse(num):
	num_list = list(str(num))
	new_list = []
	temp = 1
	while temp - 1 < len(num_list):
		new_list[len(num_list):] = num_list[0 - temp]
		temp = temp + 1
	print(new_list)
	return new_list

def is_palindrome(num):
	num_list = list(str(num))
	list2 = reverse(num)
	if num_list == list2:
		print("It is a palindrome.")
		return True
	else:
		print("It is not a palindrome.")
		return False

def count_digits(num):
	num_list = list(str(num))
	print(len(num_list))
	return len(num_list)

def sum_digits(num):
	num_list = list(str(num))
	sum = 0
	for index in num_list:
		sum = sum + int(index)
	print(sum)
	return sum

def print_menu():
	print("1) Count digits")
	print("2) Sum digits")
	print("3) Is palindrome")
	print("4) Reverse")
	print("5) Exit")

def main():
	choice = 0
	print_menu()
	while choice != 5:
		choice = int(input("Choice: "))
		if choice == 1:
			digits = int(input("Enter your digits: "))
			count_digits(digits)
		if choice == 2:
			digits = int(input("Enter your digits: "))
			sum_digits(digits)
		if choice == 3:
			digits = int(input("Enter your digits: "))
			is_palindrome(digits)
		if choice == 4:
			digits = int(input("Enter your digits: "))
			reverse(digits)
		print_menu()
	print("Exiting...")
main()
