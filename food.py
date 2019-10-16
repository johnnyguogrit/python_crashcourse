my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
my_foods.append('cannoli')
print(my_foods)


print("\nMy friends' favorite foods are:")
friend_foods.append('ice cream')
print(friend_foods)

print("\nThe first three items in the list are:")
print(friend_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[int(len(my_foods)/2):int(len(my_foods)/2)+3])

print("\nLast three items in the list are")
print(my_foods[-3:])

for my_food in my_foods:
	print(my_food)

for friend_food in friend_foods:
	print(friend_food)



