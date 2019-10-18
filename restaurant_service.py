class User():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0


	def describe_user(self):
		full_name = self.first_name.title() + " " + self.last_name.title()
		print("The name of user is: " + full_name + ".")
		print("More information about the user listed below: ")
		print("Age: " + str(self.age))
		print("location: " + self.location)


	def greet_user(self):
		full_name = self.first_name.title() + " " + self.last_name.title()
		print("Hello, " + full_name + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0


class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The name of this retaurant is " + self.restaurant_name.title() + ".")
		print("The recommended cuisine of this retaurant is " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		print("The restaurant is opening now!")

	def show_served_customers(self):
		print(str(self.number_served) + " customers have been served.")

	def set_number_served(self, number):
		if number > self.number_served:
			self.number_served = number
		else:
			print("You can't reset the served customers")

	def increment_number_served(self, number):
		if number >= 0:
			self.number_served += number
		else:
			print("You can't reset the served customers")

'''
new_user = User('albert', 'einstein', 23, 'princeton')
new_user.greet_user()
new_user.describe_user()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(str(new_user.login_attempts))
new_user.reset_login_attempts()
print(str(new_user.login_attempts))
'''

# restaurant_0 = Restaurant('north east dumplings', 'dumplings')
# restaurant_0.describe_restaurant()
# restaurant_0.open_restaurant()

# restaurant_1 = Restaurant('melody', 'ice cream')
# restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()

# restaurant_2 = Restaurant('si cuan hot pot', 'hot pot')
# restaurant_2.describe_restaurant()
# restaurant_2.open_restaurant()

restaurant = Restaurant('new line', "drink")
restaurant.open_restaurant()
restaurant.show_served_customers()
restaurant.set_number_served(10)
restaurant.show_served_customers()
restaurant.increment_number_served(10)
restaurant.show_served_customers()




