
prompt = "Please enter your name or quit with 'q': "
filename = "guest_book.txt" 

while True:

	user_name = input(prompt)

	if user_name == "":
		continue
	elif user_name != 'q':
		with open(filename, 'a') as fileobject:
		#with open(filename, 'w') as fileobject:
		#with open(filename, 'r+') as fileobject:
			fileobject.write(user_name.title()+"\n")
			print("Hi " + user_name.title() + ", you are welcome!")
	else:
		break

print("Thanks you for your custom!")


