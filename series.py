numbers = list(range(1,10))
for number in numbers:
	if number == 1:
		print(str(number) + "st\n")
	elif number == 2:
		print(str(number) + "nd\n")
	elif number == 3:
		print(str(number) + "rd\n")
	elif number <= 9:
		print(str(number) + "th\n")