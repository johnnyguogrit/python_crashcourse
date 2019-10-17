message = "Please enter the age of the audience: "
active = True

while active:
	age = input(message)
	if age == 'quit':
		#active = False
		break
	else:
		age = int(age)
		if age < 3:
			price = 0
		elif age < 12:
			price = 10
		elif age >= 12:
			price = 15
		print("The price of ticket for you is: " + str(price) + ".")
