#Class is a blueprint of an object
class Student:
    #class level attibute, all instances of the class have it
    school_name = "Weber State University"
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'

    def __str__(self):
        #Magic Method __str__ is a user-friendly string representation of the object
        return str(
            f"Student Info \n" f"\tFirst Name: {self.first_name} \n" f"\tLast Name: {self.last_name}\n" f"\tStudent Grade: {self.grade}\n" f"\tStudent Email: {self.email}\n" f"\tSchool Name: {Student.school_name}"
        )

    def print_student_data(self):
        print(f"Student Info \n",
              f"\tFirst Name: {self.first_name} \n",
              f"\tLast Name: {self.last_name}\n",
              f"\tStudent Grade: {self.grade}\n",
              f"\tStudent Email: {self.email}\n" ,        
              f"\tSchool Name: {Student.school_name}")

    def change_grade(self, grade):
        self.grade = str(grade)

#jay_pike is an instance of the student class
jay_pike = Student("Jay", "Pike", "Sophomore") #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior") #object of the student class
waldo_wildcat = Student("Waldo", "Wildcat", "Senior")


print(jay_pike.email)
print(jane_doe.email)
waldo_wildcat.print_student_data()

waldo_wildcat.change_grade("Freshman")

waldo_wildcat.print_student_data()

print(jay_pike)
print(jane_doe)
print(waldo_wildcat)