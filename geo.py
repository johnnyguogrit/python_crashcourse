geo_of_country = {
	'nile': 'egypt',
	'yangzi': 'china',
	'amazone': 'brasil'
}

for river, country in geo_of_country.items():
	print("The " + river.title() + " runs through " + country.title() + ".")

for river in geo_of_country.keys():
	print(river.title())

for country in geo_of_country.values():
	print(country.title())



