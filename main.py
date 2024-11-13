#Class is a blueprint of an object
class Student:
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'

    def print_student_data(self):
        print(f"Student Info \n",
              f"\tFirst Name: {self.first_name} \n",
              f"\tLast Name: {self.last_name}\n",
              f"\tStudent Grade: {self.grade}\n",
              f"\tStudent Email: {self.email}"         
              )

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
