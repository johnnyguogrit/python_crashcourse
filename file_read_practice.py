
filename = 'write_into_bigfiles.txt'

with open(filename) as fileobject:
	# contents = fileobject.read()
	
	# print("\n")
	# print(contents.rstrip())

	# print("\n")
	# for line in fileobject:
	# 	print(line)

	print("\n")
	lines = fileobject.readlines()
	for line in lines:
		print(line.replace('Python', 'C'))



