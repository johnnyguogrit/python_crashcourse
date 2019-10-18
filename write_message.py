filename = 'programming.txt'
 

with open(filename, 'a') as fileobject:
	fileobject.write("I love programming.\n")
	fileobject.write("I love creating new games.\n")
	fileobject.write("I also love finding meaning in large datasets.\n")
	fileobject.write("I love creating apps that can run in a browser.\n")

def count_words(filename):

	try:
		with open(filename) as fileobject:
			contents = fileobject.read()
	except FileNotFoundError:
		print("No such file or directory: " + filename + ".")
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

count_words(filename)
	