visitors = {}
polling_active = True

while polling_active:

	prompt = "If you could visit one place in the world, where would you go?"

	name = input("Please enter your name: ")
	destination = input("\nPlease enter your favorite destination: ")
	visitors[name] = destination

	repeat = input("Would you like to continue the poll? (yes/no)")
	if repeat == 'no':
		polling_active = False

print("\n---Poll Result---")
for name, destination in visitors.items():
	print("\t" + name.title() + "'s favorite destination is " + destination.title() + ".")
