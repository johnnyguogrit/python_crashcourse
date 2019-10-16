# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# requested_toppings = []

# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		if requested_topping == 'green peppers':
# 			print("Sorry, we are out of green peppers right now!")
# 		else:
# 			print("Adding " + requested_topping + ".")
# 	print("\nFinished making your pizza!")
# else:
# 	print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 
					'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Add " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")


