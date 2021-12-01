student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

the_list = ['Outstanding', 'Exceeds Expectations', 'Acceptable', 'Fail']

for student in student_scores:
    if student_scores[student] >= 91:
        student_scores[student] = the_list[0]
    elif student_scores[student] >= 81:
        student_scores[student] = the_list[1]
    elif student_scores[student] >= 71:
        student_scores[student] = the_list[2]
    else:
        student_scores[student] = the_list[3]

print(student_scores)