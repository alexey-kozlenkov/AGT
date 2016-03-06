__author__ = 'Alexey'
from functions import read_data, assign_students

students, universities, student_priorities, university_priorities, university_capacities = read_data('input2.txt')

print("Student priorities: " + str(student_priorities))
print("University priorities: " + str(university_priorities))
print("University capacities: " + str(university_capacities))

result_assign = assign_students(students, universities, student_priorities, university_priorities,
                                university_capacities)
print "\nStable matching: %s" % str(result_assign)
