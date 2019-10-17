#show list of magician name
def show_magician(magician_names):
	for magician_name in magician_names:
		print(magician_name)

def make_great(magician_names):
	for count in range(0,len(magician_names)):
		magician_names[count] = magician_names[count].title() + " the Great"

	return magician_names

magician_name_list = ['alex', 'tom', 'ben']
new_magician_name_list = []

new_magician_name_list = make_great(magician_name_list[:])
show_magician(magician_name_list)
show_magician(new_magician_name_list)





