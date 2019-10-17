
available_car_types = ['bmw', 'toyota', 'honda', 'sabaru']
prompt = "Which kind of car would you like to rent? "

car_type = input(prompt)
if car_type in available_car_types:
	print("Let me see if I can find a " + car_type + " for you.")
else:
	print("The " + car_type.title() + " is unavailable now.")

message = "How many guests will have the supper? "
number_of_guest = input(message)
number_of_guest = int(number_of_guest)
if number_of_guest > 8:
	print("Sorry, we can't accomodate so many guests.")
else:
	print("You are welcome!")

message = "Please enter a number: "
number = input(message)
number = int(number)
if number % 10 == 0:
	print("The number " + str(number) + " is multiply of 10.")
else:
	print("The number " + str(number) + " is not multiply of 10.")






