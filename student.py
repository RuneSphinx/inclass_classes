#Class is a blueprint of an object
class Student:
    #class level attibute, all instances of the class have it
    school_name = "Weber State University"
    all_students = [] #class attribute to store all instances of the class
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade, student_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'
        self.student_id = self.format_student_id(student_id)
        Student.all_students.append(self)

    def __str__(self):
        #Magic Method __str__ is a user-friendly string representation of the object
        return str(
            f"\033[31;1;4mStudent Info \n\033[0m" f"\tFirst Name: {self.first_name} \n" f"\tLast Name: {self.last_name}\n" f"\tStudent Grade: {self.grade}\n" f"\tStudent Email: {self.email}\n" f"\tSchool Name: {Student.school_name}" f"\tID: {self.student_id}"
        )
   
    @staticmethod
    def format_student_id(student_id):
        #format student_id so it starts wtih wsu
        return f"WSU-{student_id}" if student_id else "No ID assigned"

    @classmethod #python decorator
    def from_full_name(cls, full_name, grade, id):
        firstname, lastname = full_name.split()
        return cls(firstname, lastname, grade, id)

    @classmethod 
    def get_all_students(cls):
        #class method to access the list of all students
        return cls.all_students


    def print_student_data(self):
        print(f"Student Info \n",
              f"\tFirst Name: {self.first_name} \n",
              f"\tLast Name: {self.last_name}\n",
              f"\tStudent Grade: {self.grade}\n",
              f"\tStudent Email: {self.email}\n" ,        
              f"\tSchool Name: {Student.school_name}\n",
              f"\tID: {self.student_id}")

    def change_grade(self, grade):
        self.grade = str(grade)