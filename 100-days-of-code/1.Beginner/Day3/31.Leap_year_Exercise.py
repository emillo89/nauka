"""Instructions
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4
**except** every year that is evenly divisible by 100
**unless** the year is also evenly divisible by 400
e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.
But the year 2100 is not a leap year because:
2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)"""

# 🚨 Don't change the code below 👇
check_year = int(input("What year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if check_year % 4 == 0:
    if check_year % 100 == 0:
        if check_year % 400 == 0:
            print(f"The year {check_year} is Leap")
        else:
            print(f"The year {check_year} is not leap")
    else:
        print(f"The year {check_year} is Leap")
else:
    print(f"The year {check_year} is not leap")