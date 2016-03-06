__author__ = 'Alexey'


def read_data(path):
    file = open(path)
    students = file.readline().strip().split(" ")
    universities = file.readline().strip().split(" ")
    university_capacities = {}
    capacities = file.readline().strip().split(" ")
    for i in range(len(capacities)):
        university_capacities[universities[i]] = int(capacities[i])

    file.readline().strip()
    student_priorities = {}
    for student in students:
        student_priorities[student] = file.readline().strip().split(" ")

    file.readline().strip()
    university_priorities = {}
    for university in universities:
        university_priorities[university] = file.readline().strip().split(" ")

    yield students
    yield universities
    yield student_priorities
    yield university_priorities
    yield university_capacities


def assign_students(students, universities, student_priorities, university_priorities, university_capacities):
    """
    :type students: list
    :type universities: list
    :type student_priorities: dict
    :type university_priorities: dict
    :type university_capacities: dict
    """
    result = {university: [] for university in universities}
    while students:
        student_to_assign = students[0]
        prior_university = student_priorities[student_to_assign].pop(0)
        if university_capacities[prior_university]:
            university_capacities[prior_university] -= 1
            result[prior_university].append(student_to_assign)
            students.remove(student_to_assign)
        else:
            student_to_kick = find_silly_student(student_to_assign, prior_university, university_priorities, result)
            if student_to_kick:
                result[prior_university].remove(student_to_kick)
                students.append(student_to_kick)

                result[prior_university].append(student_to_assign)
                students.remove(student_to_assign)
    return result


def find_silly_student(student, university, priorities, result):
    opponents = result[university]
    students_range = priorities[university]
    index = students_range.index(student)
    for opponent in opponents:
        if students_range.index(opponent) > index:
            return opponent
    return None
