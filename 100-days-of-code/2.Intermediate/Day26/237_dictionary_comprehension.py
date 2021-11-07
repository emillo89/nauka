import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_score = {student : random.randint(1,100) for student in names }
print(students_score)

passed_students = {key: value for (key, value) in students_score.items() if value >= 60}
print(passed_students)