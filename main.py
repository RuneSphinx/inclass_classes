from student import Student
from graduate_student import Graduate_Student

#jay_pike is an instance of the student class
jay_pike = Student.from_full_name("Jay Pike", "Sophomore", 3456) #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior", 1234) #object of the student class
waldo_wildcat = Student("Waldo", "Wildcat", "Senior")
grad_student_1 = Graduate_Student("Michael", "Scott", "Graduate")


# print(jay_pike.email)
# print(jane_doe.email)
# waldo_wildcat.print_student_data()
# waldo_wildcat.change_grade("Freshman")
# waldo_wildcat.print_student_data()

# print("Printing out object")
# print(jay_pike)
# print(jane_doe)
# print(waldo_wildcat)

all_students_in_class = Student.get_all_students()
for student in all_students_in_class:
    student.print_student_data()