message = "Please enter your faovrite ingredients for pizza:"
active = True

while active:
	ingredient = input(message)
	if ingredient != 'quit':
		print("\nWe will add " + ingredient.title() + " in pizza.")
	else:
		print("\nThe pizza will be ready soon!")
		active = False
