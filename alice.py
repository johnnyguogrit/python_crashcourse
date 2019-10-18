filename = 'alice.txt'

try:
	with open(filename) as fileobject:
		contents = fileobject.read()
except FileNotFoundError:
	print("No such file or directory: " + filename + ".")