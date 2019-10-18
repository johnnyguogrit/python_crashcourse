filename = 'data/pi_digits.txt'
#filename = 'data\pi_digits.txt'


'''
# open file with blank line
with open(filename) as file_object:

	contents = file_object.read()
	print(contents)
'''

'''
# open file without blank line

with open(filename) as file_object:

	contents = file_object.read()
	print(contents)
	print(contents.rstrip())

'''

'''
# open file per lines

with open(filename) as file_object:

	#contents = file_object.read()

	for line in file_object:
		#print(line)
		print(line.rstrip())
'''


# open file per lines
with open(filename) as file_object:
	lines = file_object.readlines()

	pi_string = ''

	for line in lines:
		pi_string += line.rstrip()
		print(pi_string)

	print("\nThe final string we got is:")
	print(pi_string)



# open file per lines
with open(filename) as file_object:
	lines = file_object.readlines()

	pi_string = ''

	for line in lines:
		pi_string += line.strip()
		print(pi_string)

	print("\nThe final string we got is:")
	print(pi_string)



'''
	birthday = input("\nPlease enter your birthday in the form mmddyy: ")
	if birthday in pi_string:
		prnit("Your birthday appears in the first million digits of pi")
	else:
		prnit("Your birthday doesn't appear in the first million digits of pi")
'''
