class User:
    def __init__(self, name):
        self.name = name

class Teacher(User):
    def __init__(self, name, subject):
        User.__init__(self , name)
        self.subject = subject
    def __repr__(self):
        return f"{self.name}"
class Course:
    def __init__ (self, course_name, course_code, teacher:Teacher ):
        self.course_name = course_name
        self.course_code = course_code
        if teacher.subject == self.course_name:
            self.teacher = teacher
        else: self.teacher = "unknown"
    def __repr__(self):
        return f"Course Name: {self.course_name}, Course Code: {self.course_code}, Teacher: {self.teacher}"
        
class Student(User):
    def __init__(self, name, age, grade):
        User.__init__(self, name)
        self.age = age
        self.grade = grade
        self.course = []
        
    def display(self):
        print (f"Student Name: {self.name}, Student Grade: {self.grade}, Student Age: {self.age},Courses: {self.course} ")

eleni = Teacher ("Eleni" , "FOP")
abdi =   Teacher ("Abdi" , "OOP")
fop= Course ("FOP" , "SE2109" , eleni)
oop = Course ("OOP" , "SE2180" , abdi)
dsa = Course ("DSA" , "SE9809" , abdi) # wrong teacher
student = Student ("ROBEL" , 21 , 4)
student.course.append(fop)
student.course.append(oop)
student.course.append(dsa)
student.display()