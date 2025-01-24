#CSD-1233-01
#Assignment 2
#Name: Unni Krishna Prasad Endla
#Jan 28, 2024


#user input for year
year=int(input("Enter the year: "))

#logic to find the year for the respective animals using modulus
if year % 12 == 8:
	print(year,"is the year of Dragon")
elif year % 12 == 9:
	print(year,"is the year of Snake")
elif year % 12 == 10:
	print(year,"is the year of Horse")
elif year % 12 == 11:
    print(year,"is the year of Sheep")
elif year % 12 == 0:
    print(year,"is the year of Monkey")
elif year % 12 == 1:
    print(year,"is the year of Rooster")
elif year % 12 == 2:
    print(year,"is the year of Dog")
elif year % 12 == 3:
    print(year,"is the year of Pig")
elif year % 12 == 4:
    print(year,"is the year of Rat")
elif year % 12 == 5:
    print(year,"is the year of Ox")
elif year % 12 == 6:
    print(year,"is the year of Tiger")
elif year % 12 == 7:
    print(year,"is the year of Hare")