alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

aliens = []
for alien_numner in range(30):
	new_alien = {'color': 'green', 'points': 5}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

print("Total number of aliens: " + str(len(aliens)) + ".")

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[:5]:
	print(alien)
	

