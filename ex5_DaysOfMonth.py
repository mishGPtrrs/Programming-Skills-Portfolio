# days of month

#make a dictionary that contains the months and the amount of days within them
daysinmonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

#initialize the user's input
month = int(input("enter your month (1-12): "))

#determine the month of user's input, print days of month if valid number is entered
if 1 <= month <= 12:
    print(f"the month {month} has {daysinmonth[month]} days")
else:
    print("month not found.")
