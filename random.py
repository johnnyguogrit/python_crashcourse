from random import randint

class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		number = randint(1,self.sides)
		print("Bingo, you have rolled to " + str(number) + ".")

my_die = Die()
my_die.roll_die()

my_die = Die(10)
my_die.roll_die()

my_die = Die(20)
my_die.roll_die()

