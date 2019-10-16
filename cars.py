cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

string1 = 'short_string'
string2 = 'long_string'
if string1 == string2:
	print("Two strings are identical.")
else:
	print("Two strings are different.")

name1 = 'Alice'
name2 = 'alice'
if name1.lower() == name2.lower():
	print("The similar user was found!")
else:
	print("It is allowed to pass.")

