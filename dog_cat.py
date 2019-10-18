
filenames = ['dog.txt', 'cats.txt']
words = []

try:
	for filename in filenames:
		with open(filename, 'r') as fileobject:
			contents = fileobject.read()
			print(contents)
			print("\n")

			words = contents.split()
			print("About " + str(len(words)) + " words in " + filename + ".")

			count = contents.lower().count('t')
			print("Total " + str(count) + " 't' in " + filename + ".")			

except FileNotFoundError:
	# print("Sorry, " + filename + " was not found!")
	pass

