year = int(input("Enter the year: "))
leap = False
if year % 4==0 and year % 100!=0 or year % 400==0:
    leap = True
else:
    leap = False
if(leap):
    print("{} is leap year!".format(year))
else:
    print("{} is not a leap year!".format(year))