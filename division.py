

print("Give me tow numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break

	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break

	#anwser = int(first_number)/int(second_number)

	try:
		anwser = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(anwser)


	


