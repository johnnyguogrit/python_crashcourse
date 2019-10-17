favorite_language = {
	'jen': 'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

# print("Sarah's favorite language is " +
# 	favorite_language['sarah'].title() +
# 	"."
# 	)

for name, language in favorite_language.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

friends = ['phil', 'sarah']
for name in sorted(favorite_language.keys()):
	print(name.title())

	if name in friends:
		print("Hi" + name.title() +
			", I see your favorite language is " +
			favorite_language[name].title() + "."
			)

if 'erin' not in favorite_language.keys():
	print("Erin, please take our poll!")

print("The following languages have been mentioned:")
for language in set(favorite_language.values()):
	print(language.title())

potential_participants = ['jen', 'susan', 'tom']
for participant in favorite_language.keys():
	if participant in potential_participants:
		print("Thanks for your participation of the poll! " + participant.title())
	else:
		print("Hi! " + participant.title() + ", you are welcome to take the poll!")

