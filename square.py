squares = []
for value in range(1,11):
#	square = value**2
	squares.append(value**2)

print(squares)

digits = list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**3 for value in range(1,11)]
print(squares)

for value in range(1,21):
	print(value)

long_number_list = [value for value in range(1,1000001)]
#print(long_number_list)

print(sum(long_number_list))

odd_list = list(range(1, 20, 2))
print(odd_list)

dvide_by_3_list = [value*3 for value in range(1,11)]
print((dvide_by_3_list))

cube_list = [value**3 for value in range(1,11)]
print(cube_list)