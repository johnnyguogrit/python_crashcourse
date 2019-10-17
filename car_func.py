def build_car_info(manufacture, type, **car_extra_info):

	car_profile = {}
	car_profile['manufacture'] = manufacture
	car_profile['type'] = type
	for key, value in car_extra_info.items():
		car_profile[key] = value

	return car_profile

new_car = build_car_info('toyota', 'land cruiser', 
						color = 'white', 
						accessories = 'navigation system',
						auto_pilot = True)

print(new_car)

