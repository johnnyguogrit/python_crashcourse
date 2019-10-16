# users = ['tom', 'jack', 'jimmy', 'frank', 'admin']
users = []
login_user = 'tom'
if users:
	for user in users:
		if user == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + user + ", thank you for logging in again")
else:
	print("We need to find some users!")

current_users = ['TOM', 'jack', 'jimmy', 'frank', 'admin']
new_users = ['tom', 'ben', 'sam', 'admin', 'bony']


for new_user in new_users:
	for current_user in current_users:
		if new_user.lower() == current_user.lower():
			print("Please enter into other users, as " + new_user + " has been used.")
		else:
			print("This user " + new_user + " hasn't been used yet.")

