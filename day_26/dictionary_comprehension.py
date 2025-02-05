import random

# new_dict = {new_key : new_value for item in list}
names = ["ladu", "lili", "mina", "ladubai"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# new_dict = {new_key : new_value for (key, value) in dict.items()}
passed_students = {student:score for student, score in student_scores.items() if score > 30}
print(passed_students)





