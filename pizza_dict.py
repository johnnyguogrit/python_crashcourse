pizza = {
	'crust': 'thick',
	'toppings': ['mushroom', 'extra_cheese'],
}

print("You ordered a " + pizza['crust'] + "- curst pizza " +
	"with the following toppings:"
	)

for topping in pizza['toppings']:
	print("\t" + topping.title())

favorite_language = {
	'jen': ['python', 'c'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
}

for name, languages in favorite_language.items():
	print("\n" + name.title() + "'s favorite language are: ")
	for language in languages:
		print(language.title())



