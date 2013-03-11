#This program allows the user to pick a number between 1 and 31 in a month

#when the number is picked, it should show the day of the week it corresponds to provided the first day of the month is Sunday.

number = raw_input("Enter number: ")
date = "smtwTfS"*5
date = date[int(number)-1]
print date
