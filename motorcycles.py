motorcycles = ['honda', 'yamaha', 'suzki']
print(motorcycles)
#motorcycles[0] = 'ducati'
motorcycles.append('ducati')
print(motorcycles)

pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

empty = []
empty.append('first')
empty.append('second')
empty.append('third')
empty.insert(0, 'primary')
print(empty)

