#deliver welcome message to specific user
def greeet_user(username):
	print("Hello, " + username.title() + "!")

greeet_user('jack')

#display what you are going to learn in this chapter
def display_message():
	print("I will learn how function will work in python.")

display_message()

#favorite book
def favorite_book(title):
	print("One of my favorite book is " + title.title() + ".")

favorite_book('gone girl')

def describe_pet(pet_name, animal_type = 'dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('jessica', 'cat')
describe_pet(pet_name = 'fifteen')
describe_pet('hans')

#T-shirt
def make_shirt(size = 'large', words = 'I love python'):
	print("\nThe size of T-shirt is " + size + ".")
	print("The following sentence will be printed on T-shirt:")
	print(words)

make_shirt('middle', 'grit')
make_shirt('small', 'never give up!')
make_shirt()
make_shirt('middle')
make_shirt(words = 'follow your heart!')

#display the description of city
def describe_city(city_name, country_name = 'china'):
	print(city_name.title() + " is in " + country_name.title() + ".")

describe_city('shenzhen')
describe_city('shanghai')
describe_city('chengdu')
describe_city('paris', 'french')
describe_city(country_name = 'america', city_name = 'portland')

#construct information about one person
def build_person(first_name, last_name, age=''):
	person = {'first_name':first_name, 'last_name':last_name}
	if age:
		person['age'] = age

	return person

musician = build_person('jimmy', 'carter', age = 23)
print(musician)





