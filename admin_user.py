class User():
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location

	def describe_user(self):
		full_name = self.first_name.title() + " " + self.last_name.title()
		print("The name of user is: " + full_name + ".")
		print("More information about the user listed below: ")
		print("Age: " + str(self.age))
		print("location: " + self.location)


	def greet_user(self):
		full_name = self.first_name.title() + " " + self.last_name.title()
		print("Hello, " + full_name + "!")


class Privileges():
	def __init__(self, privileges = ['can add post']):
		self.privileges = privileges

	def show_privileges(self):
		print("The privileges of the admin is: ")
		for privilege in self.privileges:
			print("\t-" + privilege)

class Admin(User):

	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.privileges = Privileges()

new_admin = Admin('jimmy', 'carter', 45, 'new york')
new_admin.privileges.show_privileges()


