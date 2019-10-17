#dictionary emmbedded in list
familar_people_0 = {
	'first_name': 'jackie',
	'last_name': 'cao',
	'age': 37,
	'city': 'shenzhen',
}

familar_people_1 = {
	'first_name': 'susan',
	'last_name': 'ma',
	'age': 25,
	'city': 'chongqing',
}

familar_people_2 = {
	'first_name': 'ben',
	'last_name': 'gao',
	'age': 18,
	'city': 'taiyuan',
}

familar_persons = [familar_people_0, familar_people_1, familar_people_2]
for familar_person in familar_persons:
	print(familar_person)

#dictionary emmbedded in list
jessica = {
	'type': 'cat',
	'host': 'johnny',
}

fifteen = {
	'type': 'dog',
	'host': 'jackie',
}

pets = [jessica, fifteen]

for pet in pets:
	print("The " + pet['type'] + " is belong to " + pet['host'] + ".")

# list embedded in dictionary
favorite_places = {
	'johnny':['new york', 'portland', 'los angles'],
	'jackie':['hong kong', 'chong qing', 'paris'],
	'scarlet':['tokyo', 'shenzhen', 'chong qing'],
}

for name, places in favorite_places.items():
	print(name.title() + "'s favorite places are: ")
	for place in places:
		print("\t" + place.title())

favorite_numbers = {
	'johnny':[5, 8, 9],
	'jackie':[3, 6, 9],
	'scarlet':[3, 5, 8],
}

for name, numbers in favorite_numbers.items():
	print(name.title() + "'s favorite numbers are: ")
	for number in numbers:
		print("\t" + str(number))

# embedded dictionary in dictionary
cities = {
	'shenzhen': {
		'country': 'china',
		'population': 20000000,
		'fact': 'It is the most fast-growning city of the country.',
	},

	'beijing': {
		'country': 'china',
		'population': 25000000,
		'fact': 'It is the politcal and culture center of the country.',
	},

	'shanghai': {
		'country': 'china',
		'population': 30000000,
		'fact': 'It is the economical center of the country.',
	}	
}

for city_name, city_info in cities.items():
	print("The information about " + city_name.title() + " are:")
	for country, population, fact in city_info.items(): #ValueError: not enough values to unpack (expected 3, got 2)
		print("Country: " + country.title())
	# print("\tCountry: " + city_info['country'])
	# print("\tPopulation: " + str(city_info['population']))
	# print("\tFact: " + city_info['fact'])












