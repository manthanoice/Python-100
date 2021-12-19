import random

the_names = ['Okarinnn', 'Shizume', 'Daru', 'Maho', 'Mikasa', 'Eren Yeger']

the_dict = {student:random.randint(10, 50) for student in the_names}

print(the_dict)

passed_students = {student:score for (student, score) in the_dict.items() if score > 30}

print(passed_students)