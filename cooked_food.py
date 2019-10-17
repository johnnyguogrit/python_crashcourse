sandwich_orders = ['tuna', 'pastrami', 'pepperoni', 'pastrami', 'howaii', 'pastrami']
finished_sandwiches = []

print("All of pastrami are sold out")
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print("I made your " + finished_sandwich.title() + " sandwich.")
	finished_sandwiches.append(finished_sandwich)

print("All of the sandwiches you orderd are ready.")
print("---Finished Sandwiches---")
for finished_sandwich in finished_sandwiches:
	print("\t" + finished_sandwich.title() + "sandwich")
