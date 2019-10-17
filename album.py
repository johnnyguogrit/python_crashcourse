def make_album(singer_name, album_name, number_of_songs=''):
	album_info = {'singer_name':singer_name, 'album_name':album_name}

	if number_of_songs:
		album_info['number_of_songs'] = number_of_songs 

	return album_info
	

while True:
	print("Thanks for your participation of this poll about your favorite singer and song!")
	singer_name = input("Please enter your faovirte singer's name: ")
	message = input("If you want to quit, please enter 'q': ")
	if message == 'q':
		break

	album_name = input("Please enter the recommended album of this singer: ")
	message = input("If you want to quit, please enter 'q': ")
	if message == 'q':
		break

	number_of_songs= input("Do you know how many songs in this album? ")
	message = input("If you want to quit, please enter 'q': ")
	if message == 'q':
		break

	poll_result = make_album(singer_name, album_name, number_of_songs)
	print(poll_result)
	