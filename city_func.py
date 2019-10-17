def city_country(city_name, country_name):
	print("___________________________________________")
	print(city_name.title(), country_name.title())
	print("___________________________________________")

city_country('shanghai', 'china')
city_country('london', 'england')
city_country('los angels', 'america')

def make_album(singer_name, album_name, number_of_songs=''):
	album_info = {'singer_name':singer_name, 'album_name':album_name}

	if number_of_songs:
		album_info['number_of_songs'] = number_of_songs 

	return album_info

album_0 = make_album('alex', 'gun powder')
print(album_0)
album_1 = make_album('sam', 'rose', 23)
print(album_1)
album_2 = make_album('frank', 'moon', 100)
print(album_2)