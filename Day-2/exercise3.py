age = int(input("Enter your age: "))
years_left = 90 - age
days = years_left * 365
weeks = years_left * 52
months = years_left * 12
print("You have {} days, {} weeks and {} months left".format(days, weeks, months))