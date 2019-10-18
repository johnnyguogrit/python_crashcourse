import json

prompt = "Please enter your favorite number or 'q' to quit: "
filename = 'favorite_number.txt'


def load_favorite_number():
	
	try:
		with open(filename) as f_obj:
			old_number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return old_number

def input_favorite_number():

	new_number = input(prompt)
	try:
		new_number = int(new_number)
	except ValueError:
		if new_number == 'q':
			return None
		else:
			print("Please enter digit number instead of string.")
			return None
	else:
		with open(filename, 'w') as f_obj:
			json.dump(new_number, f_obj)

		return new_number

def query_favorite_number():

	favorite_number = load_favorite_number()
	if favorite_number:
		print("I know your favorite number! It's " + str(favorite_number))
	else:
		favorite_number = input_favorite_number()
		if favorite_number:
			print("I will remember you favorite number " + str(favorite_number) + ".")
		else:
			print("Sorry, I don't get your point.")

query_favorite_number()

	

