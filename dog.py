class Dog():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title()+ " is now sitting.")

	def rollover(self):
		print(self.name.title()+ " rolled over.")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.rollover()

your_dog = Dog('lucy', 9)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog's age is " + str(your_dog.age) + " years old.")