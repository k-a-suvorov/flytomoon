import time
try:

	print(''''Program to simple calculate to flight time to the moon
			Type 666 to exit''')

	#initialize block
	distance = 384403
	exitProgram = 666
	check = True

	#input block
	fuel = int(input('Enter the fuel type: 1 = chemical (up to 11.2 km/s), 2 = nuclear (up to 25 km / s) '))
	v = int(input('Enter the approximate km/s speed of your rocket: '))

	#processing and output blocs

	timeToMoon = time.strftime("%d:%H:%M:%S", time.gmtime((distance / v) * 9))

	if ((fuel == 0) or (fuel < 0) or (fuel > 2)):
		print('You din\'t choice type rocket\'s fuel, goodbye!')
		check = False
	elif ((fuel == exitProgram) or (v == exitProgram)):
		print('GoodBye!')
		check = False
	else:
		if (fuel == 1):

			print('You chose chemical rocket fuel')
			if (v < 0):
				print('There is no such speed!')
				check = False
			elif(v == 0):
				print('The Speed of rocket = ', v, 'We don\'t flight now!' )
				check = False
			elif ((v > 0) and (v < 8)):
					print(F"We can get off the Ground and then land.")
			elif ((v > 8) and (v <= 12)):
				print(F"The travel time in days will be {timeToMoon}")
			elif (v > 12):
				print(F"While such speeds are not possible!")

		else:
			if (fuel == 2):
				print('You chose nuclear rocket fuel')
			if (v < 0):
				print('There is no such speed!')
				check = False
			elif(v == 0):
				print('The Speed of rocket = ', v, 'We don\'t flight now!' )
				check = False
			elif ((v > 0) and (v < 8)):
					print(F"We can get off the Ground and then land.")
			elif ((v > 8) and (v < 12)):
				print(F"The travel time in days will be {timeToMoon}")
			elif ((v > 12) and (v <= 25)):
				print(F"The travel time in days will be {timeToMoon}")
			elif (v > 25):
				print(F"While such speeds are not possible!")


except ValueError:
    print('We have some mistakes of userinput current value!')
except TypeError:
    print('We have some mistakes of userinput current type!')
except SystemError:
	print('The system mistakes are found in this program')
