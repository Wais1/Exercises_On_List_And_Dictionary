#Exercise 4

eren = {
    "name": "Eren",
    "homework": [90.0,97.0,75.0,92.0],
    "quizzes": [88.0,40.0,94.0],
    "tests": [75.0,90.0],
}
mikasa = {
    "name": "Mikasa",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0],
}
armin = {
    "name": "Armin",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0],
}

students = [eren, mikasa, armin]

for student in students:
    print(student["name"])
    print(student["homework"])
    print(student["quizzes"])
    print(student["tests"])

def average(numbers):
    total = sum(numbers)
    return total/len(numbers)

def get_average(student):
    homework = average(student["homework"]) * 0.10
    quizzes = average(student["quizzes"]) * 0.30
    tests = average(student["tests"]) * 0.60
    return homework + quizzes + tests

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
print(get_letter_grade(get_average(mikasa)))

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

class_average = get_class_average(students)

print(class_average)
print(get_letter_grade(class_average))