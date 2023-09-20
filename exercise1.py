'''
Name: Edgar Mendez
KUID: 3048729
DATE: 11/5/2021
Purpose: Matrix Data
Lab: 07
Last modified: 11/5/2021
'''

def average():
	temp = []
	line1 = []
	line2 = []
	line3 = []
	line4 = []
	input_file = open("input.txt")
	for line in input_file:
		if line4 == line3:
			line4 = line.split(" ")
			if line3 == line2:
				line3 = line.split(" ")
				if line2 == line1:
					line2 = line.split(" ")
					if line1 == temp:
						line1 = line.split(" ")
	avr1 = 0
	for index in line1:
		avr1 = avr1 + int(index)
	avr1 = avr1/len(line1)
	avr2 = 0
	for index in line2:
		avr2 = avr2 + int(index)
	avr2 = avr2/len(line2)
	avr3 = 0
	for index in line3:
		avr3 = avr3 + int(index)
	avr3 = avr3/len(line3)
	avr4 = 0
	for index in line4:
		avr4 = avr4 + int(index)
	avr4 = avr4/len(line4)
	total_avr = (avr1 + avr2 + avr3 + avr4)/4
	input_file.close()
	average_file = open("averages.txt", "w")
	average_file.write("Total average: "+str(total_avr))
	average_file.write("\nRow 1 average: "+str(avr1))
	average_file.write("\nRow 2 average: "+str(avr2))
	average_file.write("\nRow 3 average: "+str(avr3))
	average_file.write("\nRow 4 average: "+str(avr4))
	average_file.close()

def reverse_list(list):
	old_list = list
	new_list = []
	temp = 1
	while temp - 1 < len(old_list):
		new_list[len(old_list):] = old_list[0 - temp]
		temp = temp + 1
	return new_list


def reverse():
	temp = []
	line1 = []
	line2 = []
	line3 = []
	line4 = []
	input_file = open("input.txt")
	for line in input_file:
		if line4 == line3:
			line4 = line.split(" ")
			if line3 == line2:
				line3 = line.split(" ")
				if line2 == line1:
					line2 = line.split(" ")
					if line1 == temp:
						line1 = line.split(" ")
	line1 = reverse_list(line1)
	line2 = reverse_list(line2)
	line3 = reverse_list(line3)
	line4 = reverse_list(line4)
	input_file.close()
	reverse_file = open("reverse.txt", "w")
	reverse_file.write(str(line1))
	reverse_file.write("\n"+str(line2))
	reverse_file.write("\n"+str(line3))
	reverse_file.write("\n"+str(line4))
	reverse_file.close()

def flipped():
	temp = []
	line1 = []
	line2 = []
	line3 = []
	line4 = []
	input_file = open("input.txt")
	for line in input_file:
		if line4 == line3:
			line4 = line.split(" ")
			if line3 == line2:
				line3 = line.split(" ")
				if line2 == line1:
					line2 = line.split(" ")
					if line1 == temp:
						line1 = line.split(" ")
	input_file.close()
	flipped_file = open("flipped.txt", "w")
	flipped_file.write(str(line4))
	flipped_file.write("\n"+str(line3))
	flipped_file.write("\n"+str(line2))
	flipped_file.write("\n"+str(line1))
	flipped_file.close()

def diagonal():
	temp = []
	line1 = []
	line2 = []
	line3 = []
	line4 = []
	lines = 0
	input_file = open("input.txt")
	for line in input_file:
		lines = lines + 1
		if line4 == line3:
			line4 = line.split(" ")
			if line3 == line2:
				line3 = line.split(" ")
				if line2 == line1:
					line2 = line.split(" ")
					if line1 == temp:
						line1 = line.split(" ")
	if lines == len(line1) and lines == len(line2) and lines == len(line3) and lines == len(line4):
		new_line1 = [str(line1[0]), str(line2[0]), str(line3[0]), str(line4[0])]
		new_line2 = [str(line1[1]), str(line2[1]), str(line3[1]), str(line4[1])]
		new_line3 = [str(line1[2]), str(line2[2]), str(line3[2]), str(line4[2])]
		new_line4 = [str(line1[3]), str(line2[3]), str(line3[3]), str(line4[3])]
	input_file.close()
	diagonal_file = open("diagonal.txt", "w")
	diagonal_file.write(str(new_line1))
	diagonal_file.write("\n"+str(new_line2))
	diagonal_file.write("\n"+str(new_line3))
	diagonal_file.write("\n"+str(new_line4))
	diagonal_file.close()

def main()
	average()
	reverse()
	flipped()
	diagonal()

main()
