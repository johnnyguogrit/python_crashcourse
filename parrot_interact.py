prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEhter 'quit' to end the program. "

active = True
message = ""

while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)