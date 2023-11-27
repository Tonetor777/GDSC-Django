""" 
Task: Student Database

Create a simple student database program using Python dictionaries and basic data types. The program should be able to perform the following actions:

Add Student: Allow the user to add a new student to the database. Collect information such as name, age, grade, and any other relevant details.

View Student: Allow the user to view the details of a specific student by entering the student's name.

List All Students: Display a list of all students in the database with their basic information.

Update Student Information: Allow the user to update the information of a specific student, such as changing their grade or age.

Delete Student: Allow the user to delete a student from the database based on their name.
"""
import os
studentData = {} 
def add():
    os.system('cls')
    print ("Enter 'exit' in place of the name to stop adding.")
    while(True):
        print("--------------------------")
        name = input("Enter the Students Name\n")
        if (name.lower() == "exit"):
            return
        age= input("Enter the Students Age\n")
        grade = input("Enter the Students Grade\n") 
        studentData[name] = [age , grade]
""" print(studentData) """
def view():
    os.system('cls')
    if len(studentData) == 0:
        print("No Student data in the Database")
        return
    name = input("Enter the name: ").lower()
    for x in studentData:
        if x.lower() == name:
            print("--------------------------")
            print(f"Name: {x} \nAge: {studentData[x][0]} \nGrade: {studentData[x][1]}")
            return 
    print("Not Found!")

def List():
    os.system('cls')
    if len(studentData) == 0:
        print("No Student data in the Database")
        return
    i = 1
    for x in studentData:
        print("--------------------------")
        print (f"Student {i}\nName: {x} \nAge: {studentData[x][0]} \nGrade: {studentData[x][1]}\n\n")
        i += 1

def update(): 
    os.system('cls')
    name = input("Enter the name of the person you want to edit: ").lower()
    for student in studentData:
        if student.lower() == name:
            edit = int(input("Option\n1.Edit Age\n2.Edit Grade\n"))
            if edit == 1:
                studentData[student][0] = input ("Enter updated age: ")
            elif edit == 2:
                studentData[student][1] = input ("Enter updated Grade: ")
            else: print ("Wrong Input")
        return
    print ("Student not Found!")
def delete():
    os.system('cls')
    name = input("Enter the name of the person you want to delete: ").lower()
    for student in studentData:
        if student.lower() == name:
            del(studentData[student])
            print ("Successfuly Deleted!")
            return
    print ("Student not Found!")
run = 0
while run != 1:
    option = int(input("\n\tOPTIONS\n1.Add\n2.View\n3.List\n4.update\n5.Delete\n6.Exit\n"))
    if option == 1:
        add()
    elif option == 2:
        view()
    elif option == 3:
        List()
    elif option == 4:
        update()
    elif option == 5: 
        delete()
    elif option==6:
        run = 1
