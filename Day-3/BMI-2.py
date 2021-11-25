height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = round((weight/(height**2)),2)
a = 'Underweight'
b = 'Normal weight'
c = 'Overweight'
d = 'Obese'
e = 'Cinically Obese'
if bmi<18.5:
    print("Your BMI is {} and you are {}".format(bmi, a))
elif bmi>18.5 and bmi<25:
    print("Your BMI is {} and you are {}".format(bmi, b))
elif bmi>25 and bmi<30:
    print("Your BMI is {} and you are {}".format(bmi, c))
elif bmi>30 and bmi<35:
    print("Your BMI is {} and you are {}".format(bmi, d))
else:
    print("Your BMI is {} and you are {}".format(bmi, e))