height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))

if height > 3:
    raise ValueError('This is for humans, not titans lmao')

bmi = weight / height ** 2

print('Your bmi is: {}'.format(bmi))