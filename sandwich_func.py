def ingriedient(*toppings):
	print("Your pizza will be added with the following toppings:")
	for topping in toppings:
		print(topping.title())

ingriedient('green pepper', 'shrimp', 'crab')
ingriedient('tomato')
ingriedient('pork')
