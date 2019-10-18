prompt = "Please enter two number to add or quit('q')"

while True:
	try:
		first_number = input("\nFirst number: ")
		first_number = int(first_number)
	except ValueError:
		if first_number == 'q':
			break
		else:
			print("Please input digit instead of string.")
			continue
		
	try:
		second_number = input("\nSecond number: ")
		second_number = int(second_number)
	except ValueError:
		if second_number == 'q':
			break
		else:
			print("Please input digit instead of string.")
			continue

	add_number = first_number + second_number
	print(str(first_number) + " + " + str(second_number) + 
		" = " + str(add_number) )



