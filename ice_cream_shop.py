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

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def add_new_flavor(self, flavors):
		for flavor in flavors:
			self.flavors.append(flavor)
			print("New flavor of ice cream, " + flavor.title() + " was added.")

	def show_available_flavor(self):
		print("\n---List of Ice Cream Flavor---")
		for flavor in self.flavors:
			print("\t-" + flavor)


new_flavors = ['mint', 'strawberry', 'banana']
my_favorite_icereamstand = IceCreamStand('KFC', 'west')
my_favorite_icereamstand.add_new_flavor(new_flavors)
my_favorite_icereamstand.show_available_flavor()
my_favorite_icereamstand.show_served_customers()






